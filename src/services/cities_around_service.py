import requests

class CitiesAroundService:
    def __init__(self):
        pass

    def get_cities_around(self, city_name: str, distance: float):
        coordinates = self.get_coordinates(city_name)
        cities_around = self.get_cities_around_coordinates(coordinates, distance)
        return cities_around

    def get_coordinates(self, city_name: str):
        url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
        response = requests.get(url)
        data = response.json()

        if len(data) == 0:
            raise Exception(f"City {city_name} not found")

        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])
        return {"lat": latitude, "lon": longitude}

    def get_cities_around_coordinates(self, coordinates: tuple, distance: float):
        distance = distance * 1000
        url = f"https://overpass-api.de/api/interpreter?data=[out:json];(node(around:{distance},{coordinates['lat']},{coordinates['lon']})[place~\"city|town\"];rel(around:{distance},{coordinates['lat']},{coordinates['lon']})[place~\"city|town\"];);out;"
        response = requests.get(url)
        data = response.json()
        cities_around = []
        for city in data["elements"]:
            cities_around.append(city["tags"]["name"])
        return cities_around

