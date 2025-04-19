import httpx
import asyncio
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

async def get_stations():
    url = "https://catalog.api.2gis.com/3.0/items"
    params = {
        "lon": 39.95044850840618,
        "lat": 43.411637615233644,
        "type": "station_platform",
        "radius": 750,
        "key": "3150fd27-26a9-49d4-996c-bf9c11787d13"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json() 
        except httpx.RequestError as e:
            return {"error": f"Request error: {e}"}
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP error occurred: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}

@router.get("/stations")
async def get_stations_endpoint():
    data = await get_stations()
    if data:
        return JSONResponse(content=data)
    else:
        return JSONResponse(content={"error": "No data found"}, status_code=404)

# Функция для извлечения и формирования данных об остановках
async def extract_stations():
    data = await get_stations()  # Получаем данные
    if data:
        stations = []
        for item in data.get('result', {}).get('items', []):
            station = {
                'id': item.get('id'),
                'name': item.get('name'),
                'full_name': item.get('full_name'),
                'type': item.get('type')
            }
            stations.append(station)

        # Поиск остановки "Парк Сириус"
        park_sirius = next((station for station in stations if 'Парк Сириус' in station['full_name']), None)

        if park_sirius:
            print(f"Остановка: {park_sirius['name']}")
            print(f"Полное название: {park_sirius['full_name']}")
            print(f"ID: {park_sirius['id']}")
            print(f"Тип: {park_sirius['type']}")
        else:
            print("Остановка 'Парк Сириус' не найдена.")
    else:
        print("No data found")
        return []

# Основная асинхронная функция
async def main():
    await extract_stations()

# Запуск асинхронной функции main
if __name__ == "__main__":
    asyncio.run(main())