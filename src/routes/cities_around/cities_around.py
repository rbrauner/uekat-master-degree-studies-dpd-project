from fastapi import APIRouter
from src.service.cities_around_service import CitiesAroundService

cities_around_router = APIRouter()
cities_around_service = CitiesAroundService()

@cities_around_router.get("/cities-around")
async def cities_around(c: str, d: float):
    try:
        cities_around = cities_around_service.get_cities_around(c, d)
        return {"city": c, "distance": d, "cities_around": cities_around}
    except Exception as e:
        return {"error": str(e)}
