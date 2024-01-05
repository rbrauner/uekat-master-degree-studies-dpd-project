from unittest import TestCase, mock
from src.services.cities_around_service import CitiesAroundService


class TestCitiesAroundService(TestCase):
    def setUp(self):
        self.service = CitiesAroundService()

    @mock.patch('requests.get')
    def test_get_coordinates_success(self, mock_get):
        city_name = "New York"
        expected_result = {"lat": 40.7128, "lon": -74.0060}
        mock_get.return_value.json.return_value = [{"lat": 40.7128, "lon": -74.0060}]

        result = self.service.get_coordinates(city_name)

        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with(f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1")

    @mock.patch('requests.get')
    def test_get_coordinates_city_not_found(self, mock_get):
        city_name = "Nonexistent City"
        mock_get.return_value.json.return_value = []

        with self.assertRaises(Exception) as context:
            self.service.get_coordinates(city_name)

        self.assertEqual(str(context.exception), f"City {city_name} not found")
        mock_get.assert_called_once_with(f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1")
