from fastapi import APIRouter
from services.station_data import get_stations
from services.schedule_generator import generate_schedule
from services.load_predictor import predict_count
from pydantic import BaseModel
from services.route_optimizer import find_route
from models.schemas import RouteRequest

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello, World!"}

@router.get("/stations")
async def get_station_data():
    stations = await get_stations()
    return stations

@router.get("/schedule")
def get_schedule():
    schedule = generate_schedule()
    return schedule

class PredictLoadRequest(BaseModel):
    station_id: str
    image_base64: str

@router.post("/predict_load")
def predict_load(request: PredictLoadRequest):
    result = predict_count(request.station_id, request.image_base64)
    return result

@router.post("/route")
def get_route(request: RouteRequest):
    stations = []
    loads = {} 
    route, total_distance = find_route(request.origin_id, request.destination_id, stations, loads)
    return {"route": route, "total_distance_km": total_distance}