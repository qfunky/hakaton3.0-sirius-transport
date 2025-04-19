import os
from dotenv import load_dotenv

load_dotenv()

DGIS_API_KEY = os.getenv("DGIS_API_KEY")
DEFAULT_LAT = float(os.getenv("DEFAULT_LAT", 43.2371))
DEFAULT_LON = float(os.getenv("DEFAULT_LON", 39.7282))
DEFAULT_RADIUS = int(os.getenv("DEFAULT_RADIUS", 1000))