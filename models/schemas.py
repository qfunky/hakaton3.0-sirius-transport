from pydantic import BaseModel
from typing import List

class Station(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float

class ScheduleEntry(BaseModel):
    route_id: str
    stops: List[str]
    interval_min: int

class PredictLoadRequest(BaseModel):
    station_id: str
    image_base64: str

class LoadResponse(BaseModel):
    station_id: str
    predicted_people_count: int

class RouteRequest(BaseModel):
    origin_id: str
    destination_id: str

class RouteStop(BaseModel):
    station_id: str
    name: str
    predicted_load: int

class RouteResponse(BaseModel):
    route: List[RouteStop]
    total_distance_km: float