import random

def predict_count(station_id: str, image_base64: str):
    return {
        "station_id": station_id,
        "predicted_people_count": random.randint(10, 100)
    }