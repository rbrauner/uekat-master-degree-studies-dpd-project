from unittest import TestCase, mock
from fastapi.testclient import TestClient
from src.routes.cities_around.cities_around import cities_around_router
from src.service.cities_around_service import CitiesAroundService

class TestCitiesAround(TestCase):
    def setUp(self):
        self.client = TestClient(cities_around_router)
        self.service = CitiesAroundService()

    @mock.patch('src.service.cities_around_service.CitiesAroundService.get_cities_around')
    def test_cities_around_success(self, mock_get_cities_around):
        city = "New York"
        distance = 10.0
        expected_result = ["City 1", "City 2", "City 3"]
        mock_get_cities_around.return_value = expected_result

        response = self.client.get(f"/cities-around?c={city}&d={distance}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"city": city, "distance": distance, "cities_around": expected_result})
        mock_get_cities_around.assert_called_once_with(city, distance)

    @mock.patch('src.service.cities_around_service.CitiesAroundService.get_cities_around')
    def test_cities_around_exception(self, mock_get_cities_around):
        city = "Nonexistent City"
        distance = 10.0
        error_message = "City not found"
        mock_get_cities_around.side_effect = Exception(error_message)

        response = self.client.get(f"/cities-around?c={city}&d={distance}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"error": error_message})
        mock_get_cities_around.assert_called_once_with(city, distance)
