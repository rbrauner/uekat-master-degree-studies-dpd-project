import unittest
from fastapi.testclient import TestClient
from src.app import app


class TestPrimeNumberEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_check_prime_number_endpoint(self):
        test_data = [
            {"number": 2, "expected_result": {"result": "2 jest liczbą pierwszą."}},
            {"number": 11, "expected_result": {"result": "11 jest liczbą pierwszą."}},
            {"number": 16, "expected_result": {"result": "16 nie jest liczbą pierwszą."}},
            {"number": 29, "expected_result": {"result": "29 jest liczbą pierwszą."}},
            {"number": 0, "expected_result": {"result": "0 nie jest liczbą pierwszą."}},
            {"number": 1, "expected_result": {"result": "1 nie jest liczbą pierwszą."}},
            {"number": 103, "expected_result": {"result": "103 jest liczbą pierwszą."}},
        ]

        for test_case in test_data:
            with self.subTest(test_case=test_case):
                url = f"/check-prime/{test_case['number']}"
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), test_case['expected_result'])


