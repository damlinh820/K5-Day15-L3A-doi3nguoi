"""Anonymize and count the 19-question E2 survey using standard library."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


AGE_GROUPS = {
    "Dưới 18 tuổi": "under_18",
    "18 – 22 tuổi": "18_plus",
    "23 – 30 tuổi": "18_plus",
    "31 – 40 tuổi": "18_plus",
    "Trên 40 tuổi": "18_plus",
}
OCCUPATIONS = {
    "Học sinh, sinh viên": "student",
    "Nhân viên văn phòng": "office",
    "Kinh doanh, làm việc tự do": "business_or_freelance",
    "Khác": "other",
}
BUDGET_STATUSES = {
    "Có, thường xuyên": "current_regular",
    "Có, nhưng không thường xuyên": "current_irregular",
    "Đã từng nhưng hiện tại không còn": "stopped",
    "Chưa bao giờ": "never",
}
PAYMENT_APPS = (
    "MoMo", "ZaloPay", "ShopeePay",
    "Ứng dụng ngân hàng (MB Bank, Vietcombank, Techcombank...)",
    "Không sử dụng các ứng dụng trên",
)
DIFFICULTIES = (
    "Quên theo dõi chi tiêu",
    "Khó phân loại các khoản giao dịch",
    "Nội dung giao dịch khó hiểu",
    "Không biết khoản chi nào có thể cắt giảm",
    "Phát hiện vượt ngân sách quá muộn",
    "Cảnh báo chi tiêu chưa đủ thông tin",
    "Chi tiêu qua nhiều ứng dụng, khó tổng hợp",
    "Không gặp khó khăn đáng kể",
)
METHODS = (
    "Kiểm tra số dư tài khoản",
    "Xem lịch sử giao dịch",
    "Ghi chép thủ công hoặc Excel",
    "Sử dụng ứng dụng quản lý chi tiêu",
    "Ghi nhớ trong đầu",
    "Không theo dõi chi tiêu",
)
CLOSED_ANSWERS = {
    4: (
        "Nhiều lần mỗi ngày", "Khoảng một lần mỗi ngày",
        "Vài lần mỗi tuần", "Vài lần mỗi tháng",
    ),
    7: (
        "Rất thường xuyên", "Thường xuyên", "Thỉnh thoảng", "Hiếm khi",
        "Không bao giờ", "Không đặt mức chi tiêu dự kiến",
    ),
    8: (
        "Trước khi gần chạm giới hạn ngân sách",
        "Khi gần chạm giới hạn ngân sách", "Sau khi đã vượt ngân sách",
        "Khi tài khoản gần hết tiền", "Khi tổng kết chi tiêu cuối tháng",
        "Không theo dõi ngân sách", "Chưa từng gần chạm hoặc vượt ngân sách",
    ),
    11: (
        "Luôn biết rõ", "Thường xác định được",
        "Phải mất thời gian xem lại giao dịch", "Rất khó xác định",
        "Chưa từng gặp tình huống này",
    ),
    12: (
        "Rất hữu ích", "Khá hữu ích", "Bình thường", "Ít hữu ích",
        "Không hữu ích", "Chưa từng nhận được cảnh báo",
    ),
}
METRICS = {
    "forgot_tracking": DIFFICULTIES[0],
    "classification_difficulty": DIFFICULTIES[1],
    "unknown_cut_candidates": DIFFICULTIES[3],
    "insufficient_alert_information": DIFFICULTIES[5],
    "late_budget_discovery": DIFFICULTIES[4],
}
ORIGINAL_PLAN_22_COUNTS = (11, 8, 7, 4, 3, 14)


def parse_options(value, choices, respondent_id, question):
    """Match full known labels, including labels containing commas."""
    remaining = value.strip().rstrip(",").strip()
    found = []
    while remaining:
        choice = next((
            item for item in sorted(choices, key=len, reverse=True)
            if remaining == item or remaining.startswith(item + ", ")
        ), None)
        if choice is None:
            raise ValueError(
                f"Unknown answer at {respondent_id}/Q{question}; "
                "review privately before export."
            )
        found.append(choice)
        remaining = remaining[len(choice):].lstrip(", ")
    return found


def require_known(value, choices, respondent_id, question):
    if value not in choices:
        raise ValueError(
            f"Unknown answer at {respondent_id}/Q{question}; "
            "review privately before export."
        )
    return value


def read_source(path):
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        headers = reader.fieldnames or []
        question_columns = {}
        for header in headers:
            match = re.match(r"^(\d+)\.\s", header)
            if match:
                number = int(match.group(1))
                if number in question_columns:
                    raise ValueError("Duplicate question number in source.")
                question_columns[number] = header
        if set(question_columns) != set(range(1, 20)):
            raise ValueError(
                "Expected the actual Q1-Q19 survey; "
                "do not use the ten-question draft."
            )
        rows = list(reader)
    malformed = any(
        None in row or any(value is None for value in row.values())
        for row in rows
    )
    if not rows or malformed:
        raise ValueError("Empty or malformed CSV; no export written.")
    return rows, question_columns


def anonymize(rows, question_columns):
    clean = []
    signatures = defaultdict(list)
    for index, row in enumerate(rows, start=1):
        respondent_id = f"S{index:03d}"
        answers = {
            q: row[column].strip() for q, column in question_columns.items()
        }
        age = require_known(answers[1], AGE_GROUPS, respondent_id, 1)
        occupation = require_known(answers[2], OCCUPATIONS, respondent_id, 2)
        budget = require_known(answers[5], BUDGET_STATUSES, respondent_id, 5)
        apps = parse_options(answers[3], PAYMENT_APPS, respondent_id, 3)
        methods = parse_options(answers[6], METHODS, respondent_id, 6)
        difficulties = parse_options(
            answers[9], DIFFICULTIES, respondent_id, 9
        )
        closed = {q: require_known(answers[q], choices, respondent_id, q)
                  for q, choices in CLOSED_ANSWERS.items()}
        for q in (10, 16):
            require_known(
                answers[q], ("1", "2", "3", "4", "5"), respondent_id, q
            )
        flags = []
        app_conflict = PAYMENT_APPS[-1] in apps and len(apps) > 1
        if app_conflict:
            flags.append("q03_no_usage_and_app")
        if DIFFICULTIES[-1] in difficulties and len(difficulties) > 1:
            flags.append("q09_none_and_difficulty")
        if METHODS[-1] in methods and len(methods) > 1:
            flags.append("q06_no_tracking_and_method")
        profile_match = (
            AGE_GROUPS[age] == "18_plus"
            and any(app != PAYMENT_APPS[-1] for app in apps)
            and BUDGET_STATUSES[budget].startswith("current_")
        )
        original_profile_match = (
            profile_match and OCCUPATIONS[occupation] == "office"
        )
        open_kind = "blank" if not answers[19] else "not_published"
        if answers[19].casefold() in ("không", "ko", "có"):
            open_kind = "non_substantive"
        clean.append({
            "respondent_id": respondent_id,
            "adult_status": AGE_GROUPS[age],
            "occupation_group": OCCUPATIONS[occupation],
            "budget_status": BUDGET_STATUSES[budget],
            "payment_apps": " | ".join(apps),
            "usage_frequency": closed[4],
            "tracking_methods": " | ".join(methods),
            "overspend_frequency_3months": closed[7],
            "discovery_timing": closed[8],
            "difficulties": " | ".join(difficulties),
            "transaction_description_difficulty": answers[10],
            "cut_decision": closed[11],
            "current_alert_usefulness": closed[12],
            "demo_usefulness": answers[16],
            "q19_response_kind": open_kind,
            "target_profile_match": "1" if profile_match else "0",
            "original_target_profile_match": (
                "1" if original_profile_match else "0"
            ),
            "consistent_app_profile_match": (
                "1" if profile_match and not app_conflict else "0"
            ),
            "outside_team_verified": "unknown",
            "consent_in_csv": "not_asked",
            "quality_flags": " | ".join(flags),
        })
        signature = tuple(answers[q] for q in range(1, 20))
        signatures[signature].append(respondent_id)
    duplicates = [ids for ids in signatures.values() if len(ids) > 1]
    return clean, duplicates


def write_csv(path, rows, fields=None):
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields or list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def analyze(input_path, output_dir):
    raw, columns = read_source(input_path)
    rows, duplicates = anonymize(raw, columns)
    cohorts = {
        "all_received": rows,
        "first_22_comparison": rows[:22],
        "first_24_comparison": rows[:24],
        "adults_only": [
            row for row in rows if row["adult_status"] == "18_plus"
        ],
        "adult_office": [
            row for row in rows
            if row["adult_status"] == "18_plus"
            and row["occupation_group"] == "office"
        ],
        "target_profile": [
            row for row in rows if row["target_profile_match"] == "1"
        ],
        "original_target_profile": [
            row for row in rows
            if row["original_target_profile_match"] == "1"
        ],
        "target_profile_consistent_app": [
            row for row in rows
            if row["consistent_app_profile_match"] == "1"
        ],
    }
    metrics = []
    for cohort_name, cohort in cohorts.items():
        for metric, label in METRICS.items():
            count = sum(
                label in row["difficulties"].split(" | ") for row in cohort
            )
            metrics.append({
                "cohort": cohort_name, "metric": metric,
                "count": count, "N": len(cohort),
            })
        metrics.append({
            "cohort": cohort_name, "metric": "demo_score_4_or_5",
            "count": sum(
                row["demo_usefulness"] in ("4", "5") for row in cohort
            ),
            "N": len(cohort),
        })
    comparison_counts = tuple(
        item["count"] for item in metrics
        if item["cohort"] == "first_22_comparison"
    )
    metadata = {
        "source_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
        "received": len(rows),
        "cohort_sizes": {
            name: len(cohort) for name, cohort in cohorts.items()
        },
        "exact_answer_duplicate_groups": duplicates,
        "quality_flags": {
            row["respondent_id"]: row["quality_flags"]
            for row in rows if row["quality_flags"]
        },
        "q19_response_kinds": dict(Counter(
            row["q19_response_kind"] for row in rows
        )),
        "first_22_matches_original_plan_counts": (
            len(rows) >= 22 and comparison_counts == ORIGINAL_PLAN_22_COUNTS
        ),
        "profile_definitions": {
            "target_profile": "18+, reports app use and current budget",
            "original_target_profile": "target_profile plus office worker",
            "target_profile_consistent_app": (
                "target_profile without contradictory Q3 app-use answers"
            ),
        },
        "hypothesis_status": "not_evaluable_from_this_questionnaire",
        "missing_fields": [
            "outside_team", "public_quote_consent",
            "specific_case_in_last_30_days", "review_time_at_least_15_minutes",
        ],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "responses-anonymized.csv", rows)
    write_csv(output_dir / "metrics.csv", metrics)
    questions = [
        {"question_id": f"Q{q:02d}", "question": columns[q]}
        for q in range(1, 20)
    ]
    write_csv(output_dir / "questions-actual.csv", questions)
    (output_dir / "analysis.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", type=Path, required=True,
        help="Private original CSV outside the repository.",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path(__file__).parent
    )
    args = parser.parse_args()
    analyze(args.input, args.output_dir)


if __name__ == "__main__":
    main()
