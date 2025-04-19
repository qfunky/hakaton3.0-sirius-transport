import httpx
from config import DGIS_API_KEY, DEFAULT_LAT, DEFAULT_LON, DEFAULT_RADIUS

API_URL = "https://api.2gis.ru/v2.0/places/search"

async def get_stations():
    params = {
        'lat': DEFAULT_LAT,
        'lon': DEFAULT_LON,
        'radius': DEFAULT_RADIUS,
        'key': DGIS_API_KEY,
        'type': 'station',
        'fields': 'items.point,items.name,items.id'
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(API_URL, params=params)
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            if response.status_code == 200:
                data = response.json()
                stations = [{"id": item["id"], "name": item["name"], "latitude": item["point"]["lat"], "longitude": item["point"]["lon"]} for item in data["result"]]
                return stations
            else:
                print(f"Ошибка запроса: {response.status_code}, {response.text}")
                return []
        except httpx.RequestError as e:
            print(f"Ошибка запроса к 2ГИС: {e}")
            return []
        except httpx.HTTPStatusError as e:
            print(f"Ошибка HTTP: {e}")
            return []
        except httpx.TimeoutException:
            print("Таймаут при подключении к 2ГИС")
            return []
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            return []