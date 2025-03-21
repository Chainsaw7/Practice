from datetime import datetime,timedelta

from airflow import  DAG
from airflow.operators.bash import BashOperator


default_args={
        'owner': 'emmanouil.goulidakis@infologistix.de',
        'retries': 5,
        'retry_delay': timedelta(minutes=2)

        }


with DAG( 
   dag_id="My_first_dag",
   default_args=default_args,
   description='This is my first DAG example',
   start_date=datetime(2025,3,17),
   schedule_interval='@daily'
) as dag:
    task1=BashOperator(
       task_id='My_first_task',
       bash_command="echo Hello world"
       )

    task2=BashOperator(
       task_id='My_second_task',
       bash_command="echo This is the second task"
       )

    task1.set_downstream(task2)
