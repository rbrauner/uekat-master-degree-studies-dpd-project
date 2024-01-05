from fastapi import FastAPI
from src.routes.homepage.homepage import homepage_router
from src.routes.hello_world.hello_world import hello_world_router
from src.routes.cities_around.cities_around import cities_around_router

app = FastAPI(
    title="uekat-master-degree-studies-dpd-project",
    description="""
    Uniwersytet Ekonimiczny in Katowice - master degree studies - project for the subject "Dobre praktyki programowania"
    """,
    version="0.0.1",
    license_info={
        "name": "MIT",
        "url": "https://github.com/rbrauner/uekat-master-degree-studies-dpd-project/blob/main/LICENSE",
    },
)
app.include_router(homepage_router)
app.include_router(hello_world_router)
app.include_router(cities_around_router)
