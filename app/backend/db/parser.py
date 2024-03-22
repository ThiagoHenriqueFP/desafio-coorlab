import pandas

from app.backend.exception.ResourceNotFoundException import ResourceNotFoundException

df = pandas.read_json("app/backend/db/data.json")


def get_travel_by_id(travels: list, id: int):
    for travel in travels:
        if (travel["id"] == id):
            return travel


def get_travels_by_city(city: str):
    travels = []
    for travel in df["transport"]:
        if city.lower() == travel["city"].lower():
            travels.append(travel)

    economic = 1000
    fast = 100

    id_cheaper = 0
    id_faster = 0

    for travel in travels:
        price_parser: str = travel["price_econ"][2:]
        price_econ = float(price_parser)

        duration_sanitized = travel["duration"][:-1]
        duration_parsed = int(duration_sanitized)

        if price_econ < economic:
            economic = price_econ
            id_cheaper = travel["id"]
        
        if duration_parsed < fast:
            fast = duration_parsed
            id_faster = travel["id"]

    options = [
        get_travel_by_id(travels, id_faster),
        get_travel_by_id(travels, id_cheaper),
    ]


    if len(options) == 0:
        raise ResourceNotFoundException("destiny not found!")

    return options


def get_cities_list():
    cities = []
    for travel in df["transport"]:
        if travel["city"] not in cities:
            cities.append(travel["city"])

    if len(cities) == 0:
        raise ResourceNotFoundException("cities not found")

    return cities