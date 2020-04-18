"""parallel tasks dag to see concurrency"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG(
    'dummy',
    max_active_runs=1,
    default_args=default_args,
    schedule_interval='@yearly')
dag.doc_md = __doc__

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

for i in range(10):
    tasks = DummyOperator(task_id='{}'.format(i), dag=dag)
    start >> tasks >> end
