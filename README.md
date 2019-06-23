# airflow

docker pull puckel/docker-airflow

docker-compose -f docker-compose-CeleryExecutor.yml up -d

Multiple docker containers: 
Web Server >> http://localhost:8080 
Scheduler 
PostgreSQL database >> airflow initdb
Redis
Flower
Worker

Docker manager: https://kitematic.com/
