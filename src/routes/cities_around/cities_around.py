from fastapi import APIRouter
from src.services.cities_around_service import CitiesAroundService

cities_around_router = APIRouter()
cities_around_service = CitiesAroundService()


@cities_around_router.get("/cities-around")
async def cities_around(city: str, distance_km: float):
    try:
        cities_around = cities_around_service.get_cities_around(city, distance_km)
        return {"city": city, "distance": distance_km, "cities_around": cities_around}
    except Exception as e:
        return {"error": str(e)}
