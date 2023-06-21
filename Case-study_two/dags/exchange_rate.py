
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 21, 1, 0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
 }

dag = DAG(
    'exchange_rate_dag',
    default_args=default_args,
    description='Fetch exchange rates twice daily',
    schedule_interval='0 1,23 * * *',  # Run at 1 AM and 11 PM daily
 )

fetch_rates_task = BashOperator(
    task_id='fetch_rates',
    bash_command='python  /home/opeyemi/Autochek_assessment/Case-study_two/dags/exchange_rate.py',
    dag=dag
)

