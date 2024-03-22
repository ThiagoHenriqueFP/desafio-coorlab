from fastapi import FastAPI

from app.backend.exception import ResourceNotFoundException
from app.backend.db import parser
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api/travels/to/{city}")
async def get_travels(city: str):
    try:
        return parser.get_travels_by_city(city)

    except ResourceNotFoundException:
        return {"Error": "City not found", "Code": 404}


@app.get("/api/travels/cities")
async def get_cities():
    try:
        return parser.get_cities_list()

    except ResourceNotFoundException:
        return {"Error": "cities not found", "Code": 404}
