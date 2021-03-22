# airflow
```bash
git clone https://github.com/puckel/docker-airflow

docker-compose -f docker-compose-CeleryExecutor.yml up -d
```
Multiple docker containers: 

- Web Server 
  - http://localhost:8080 
- Scheduler 
- PostgreSQL database
- Redis
- Flower
- Worker
- [dag examples](https://github.com/apache/airflow/tree/master/airflow/example_dags)
- [local dev environment](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)
