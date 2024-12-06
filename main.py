from datetime import datetime
from extract import extract_data
from transform import transform_data
from load import load_data

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.8566,  # Latitude pour Paris
    "longitude": 2.3522,  # Longitude pour Paris
    "hourly": "temperature_2m",
}

def main():
    data = extract_data(url, params)
    if data:
        transformed_data = transform_data(data)
        file_path = f"data/weather_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        load_data(transformed_data, file_path)

if __name__ == "__main__":
    main()
