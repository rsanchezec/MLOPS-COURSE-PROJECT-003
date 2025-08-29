from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from airflow.hooks.base import BaseHook
from datetime import datetime
import pandas as pd
import sqlalchemy
import requests

def download_and_load():
    # Descargar datos de ejemplo (Titanic desde GitHub)
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    
    # Descargar el archivo
    response = requests.get(url)
    with open("/tmp/titanic.csv", "w") as f:
        f.write(response.text)
    
    # Cargar a PostgreSQL
    conn = BaseHook.get_connection('postgres_default')  
    engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}")
    df = pd.read_csv("/tmp/titanic.csv")
    df.to_sql(name="titanic", con=engine, if_exists="replace", index=False)
    
    print(f"Loaded {len(df)} rows to PostgreSQL")
    return "success"

with DAG(
    dag_id="simple_etl_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    
    etl_task = PythonOperator(
        task_id="download_and_load",
        python_callable=download_and_load
    )