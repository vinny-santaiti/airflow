"""
Airflow tutorial dag
https://airflow.apache.org/tutorial.html
"""

from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'vincent',
    'start_date': airflow.utils.dates.days_ago(2),
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
    }

dag = DAG(
    'tutorial',
    default_args=default_args,
    description='A tutorial DAG',
    schedule_interval='@daily',
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)

# This means that t2 will depend on t1
# running successfully to run.
t1 >> t2

# command layout: command subcommand dag_id task_id date
# airflow test tutorial print_date 2019-06-21
# airflow test tutorial sleep 2019-06-21
