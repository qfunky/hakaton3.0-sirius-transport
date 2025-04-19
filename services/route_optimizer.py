import heapq
from utils.geometry import haversine_distance

def find_route(start_station, end_station, stations, loads):
    graph = {station["id"]: [] for station in stations}
    
    for station in stations:
        for neighbor in stations:
            if station["id"] != neighbor["id"]:
                dist = haversine_distance(station["latitude"], station["longitude"], neighbor["latitude"], neighbor["longitude"])
                graph[station["id"]].append((neighbor["id"], dist))

    queue = [(0, start_station)]
    distances = {station["id"]: float("inf") for station in stations}
    distances[start_station] = 0
    previous = {station["id"]: None for station in stations}

    while queue:
        current_distance, current_station = heapq.heappop(queue)

        if current_distance > distances[current_station]:
            continue

        for neighbor_id, distance in graph[current_station]:
            load_factor = loads.get(neighbor_id, 0)
            new_distance = current_distance + distance + load_factor 
            if new_distance < distances[neighbor_id]:
                distances[neighbor_id] = new_distance
                previous[neighbor_id] = current_station
                heapq.heappush(queue, (new_distance, neighbor_id))

    route = []
    current = end_station
    while current is not None:
        route.append(current)
        current = previous[current]
    
    return route[::-1], distances[end_station]