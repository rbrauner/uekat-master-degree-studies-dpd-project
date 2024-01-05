from typing import Union
from fastapi import APIRouter

cities_around_router = APIRouter()

@cities_around_router.get("/cities-around")
async def cities_around(c: Union[str, None] = None, d: Union[int, None] = None):
    return {"city": c, "distance": d}
