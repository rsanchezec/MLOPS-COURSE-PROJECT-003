from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime

def hello_world():
    print("Hello World from Airflow!")
    return "success"

with DAG(
    dag_id="simple_test_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    
    task1 = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world
    )