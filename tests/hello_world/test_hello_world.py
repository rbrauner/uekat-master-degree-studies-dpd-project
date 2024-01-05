from fastapi.testclient import TestClient
from src.app import app


class TestHelloWolrd:
    client = TestClient(app)

    def test_hello_world(self):
        testData = [
            {"request": {"url": "/hello-world"}, "response": {"status_code": 200, "data": {"Hello": "World"}}},
        ]

        self._processTestData(testData)

    def _processTestData(self, testData):
        for td in testData:
            resp = self.client.get(td['request']['url'])
            assert resp.status_code == td['response']['status_code']
            assert resp.json() == td['response']['data']
