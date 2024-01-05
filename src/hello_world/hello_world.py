from fastapi import APIRouter

hello_world_router = APIRouter()

@hello_world_router.get("/hello-world")
async def hello_world():
    return {"Hello": "World"}
