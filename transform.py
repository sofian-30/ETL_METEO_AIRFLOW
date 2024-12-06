import pandas as pd

def transform_data(data):
    """Transformation des données extraites pour le format CSV."""
    hourly_data = data.get("hourly", {})
    timestamps = hourly_data.get("time", [])
    temperatures = hourly_data.get("temperature_2m", [])

    transformed_data = [{"date": timestamps[i], "temperature": temperatures[i]} for i in range(len(timestamps))]
    
    df = pd.DataFrame(transformed_data)
    return df
