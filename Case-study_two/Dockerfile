FROM apache/airflow:2.1.2

COPY ./dags /opt/airflow/dags
COPY ./requirements.txt /opt/airflow/requirements.txt

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt


