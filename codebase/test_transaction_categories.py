"""Kiểm thử nhận diện và ưu tiên lựa chọn nhóm trong demo local."""
import json
import os
import threading
import unittest
from urllib.request import Request, urlopen

os.environ["MODEL_PROVIDER"] = "fake"

from demo_server import Handler, HTTPServer
from transaction_categories import detect_category


class DetectionTests(unittest.TestCase):
    def test_known_clear_phrases(self):
        for description, direction, expected in (
            ("Trà sữa buổi chiều", "out", "an_uong"),
            ("do xang xe", "out", "di_lai"),
            ("Đóng tiền điện", "out", "hoa_don"),
            ("Gửi tiết kiệm tháng này", "out", "tiet_kiem"),
            ("Rút tiết kiệm", "in", "tiet_kiem"),
            ("Nhận lương tháng 9", "in", "khac"),
        ):
            with self.subTest(description=description):
                self.assertEqual(detect_category(description, direction), expected)

    def test_unknown_ambiguous_and_word_boundaries(self):
        for description in ("chuyen khoan ABC", "mua thuốc và trà sữa", "tien nhan qua"):
            with self.subTest(description=description):
                self.assertIsNone(detect_category(description, "out"))
        self.assertIsNone(detect_category("gửi tiết kiệm", "in"))

    def test_api_auto_unknown_and_manual_override(self):
        server = HTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = "http://127.0.0.1:%d" % server.server_port
        try:
            def post(description, category=""):
                data = {"user_id": "U001", "date": "2026-09-05", "amount": 10000,
                        "type": "out", "description": description, "category": category}
                request = Request(base + "/api/transaction", data=json.dumps(data).encode(),
                                  headers={"Content-Type": "application/json", "Origin": base})
                with urlopen(request) as response:
                    return json.load(response)
            auto = post("mua trà sữa")
            self.assertEqual((auto["category"], auto["classification"]), ("an_uong", "auto"))
            unknown = post("chuyen khoan ABC")
            self.assertEqual((unknown["category"], unknown["classification"]), ("chua_phan_loai", "pending"))
            manual = post("mua trà sữa", "giai_tri")
            self.assertEqual((manual["category"], manual["classification"]), ("giai_tri", "manual"))
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
