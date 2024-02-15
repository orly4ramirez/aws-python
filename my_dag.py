from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'orly_ramirez',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 14),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_daily_dag',
    default_args=default_args,
    description='A simple daily DAG',
    schedule_interval=timedelta(days=1),  # Run daily
)

# Define your tasks here
task1 = DummyOperator(task_id='task1', dag=dag)
task2 = DummyOperator(task_id='task2', dag=dag)

# Set task dependencies
task1 >> task2
