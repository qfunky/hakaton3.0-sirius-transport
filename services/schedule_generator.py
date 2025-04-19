import random

def generate_schedule():
    routes = ["R1", "R2", "R3"]
    stops = ["st_001", "st_005", "st_009"]
    
    schedule = []
    for route in routes:
        schedule.append({
            "route_id": route,
            "stops": random.sample(stops, len(stops)),
            "interval_min": random.randint(5, 15)
        })
    return schedule