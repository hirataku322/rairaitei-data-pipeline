FROM apache/airflow:2.8.2
ADD . .
RUN << EOF
  pip install poetry
  poetry install
EOF
