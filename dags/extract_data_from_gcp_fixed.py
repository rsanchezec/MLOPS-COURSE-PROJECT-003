from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from datetime import datetime
import pandas as pd
import sqlalchemy
from google.cloud import storage
import os

def download_from_gcs():
    """Download file from Google Cloud Storage using hook directly"""
    # Set up GCS client using connection
    gcp_conn = BaseHook.get_connection('google_cloud_default')
    
    # Download file
    client = storage.Client()
    bucket = client.bucket('rsc_my_bucket_003')
    blob = bucket.blob('Titanic-Dataset.csv')
    
    # Download to local temp file
    blob.download_to_filename('/tmp/Titanic-Dataset.csv')
    print("File downloaded successfully from GCS")
    return '/tmp/Titanic-Dataset.csv'

def load_to_sql():
    """Load CSV data to PostgreSQL"""
    file_path = '/tmp/Titanic-Dataset.csv'
    
    # Get PostgreSQL connection
    conn = BaseHook.get_connection('postgres_default')  
    engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}")
    
    # Load and process data
    df = pd.read_csv(file_path)
    df.to_sql(name="titanic", con=engine, if_exists="replace", index=False)
    
    print(f"Loaded {len(df)} rows to PostgreSQL")
    return "success"

# Define the DAG
with DAG(
    dag_id="extract_data_from_gcp_fixed",
    schedule=None, 
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Extract STEP...
    download_task = PythonOperator(
        task_id="download_from_gcs",
        python_callable=download_from_gcs
    )
    
    # Transform and Load STEP...
    load_task = PythonOperator(
        task_id="load_to_sql",
        python_callable=load_to_sql
    )

    download_task >> load_task