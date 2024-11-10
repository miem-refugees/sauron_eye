from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def test_func():
    print("i am test func")


with DAG(
    "my_dag", start_date=datetime(2024, 1, 1), schedule_interval="@daily", catchup=False
):
    training_model_tasks = [
        PythonOperator(
            task_id="test_func",
            python_callable=test_func,
        )
    ]

    accurate = BashOperator(task_id="is_accurate", bash_command="echo 'accurate'")

    training_model_tasks >> accurate
