"""
The following instructions are for Mac 
https://www.astronomer.io/docs/cloud/stable/get-started/quickstart

curl -sSL https://install.astronomer.io | sudo bash -s -- v0.22.0

mkdir airflow-2

cd airflow-2

astro dev init

Change Dockerfile for airflow 2
https://hub.docker.com/r/astronomerio/ap-airflow/tags?page=1&ordering=last_updated&name=2.0.0

FROM astronomerio/ap-airflow:2.0.0-buster-onbuild-22237

DOCKER_BUILDKIT=0 astro dev start|stop|kill

Airflow Webserver: http://localhost:8080
Postgres Database: localhost:5432/postgres
The default credentials are admin:admin
"""
