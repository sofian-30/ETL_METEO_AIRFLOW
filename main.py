from datetime import datetime
from extract import extract_data
from transform import transform_data
from load import load_data_to_csv, load_data_to_postgres

# URL et paramètres de l'API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.8566,  # Latitude pour Paris
    "longitude": 2.3522,  # Longitude pour Paris
    "hourly": "temperature_2m",
}

# Configuration de la base PostgreSQL
db_config = {
    "dbname": "airflow",
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    "port": "5432",
}

def main():
    # Extraction des données
    data = extract_data(url, params)
    if data:
        # Transformation des données
        transformed_data = transform_data(data)
        
        # Chemin du fichier CSV
        file_path = f"data/weather_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # Chargement dans le CSV
        load_data_to_csv(transformed_data, file_path)
        
        # Chargement dans PostgreSQL
        load_data_to_postgres(transformed_data, db_config)

if __name__ == "__main__":
    main()
