from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from extract import extract_data
from transform import transform_data
from load import load_data_to_csv, load_data_to_postgres

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.8566,
    "longitude": 2.3522,
    "hourly": "temperature_2m",
}

db_config = {
    "dbname": "airflow",
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    "port": "5432",
}

def extract(**kwargs):
    data = extract_data(url, params)
    kwargs['ti'].xcom_push(key='extracted_data', value=data)

def transform(**kwargs):
    data = kwargs['ti'].xcom_pull(key='extracted_data', task_ids='extract')
    transformed_data = transform_data(data)
    kwargs['ti'].xcom_push(key='transformed_data', value=transformed_data)

def load(**kwargs):
    transformed_data = kwargs['ti'].xcom_pull(key='transformed_data', task_ids='transform')
    file_path = f"data/weather_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    load_data_to_csv(transformed_data, file_path)
    load_data_to_postgres(transformed_data, db_config)

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='etl_meteo',
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
) as dag:
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
        provide_context=True,
    )

    extract_task >> transform_task >> load_task
