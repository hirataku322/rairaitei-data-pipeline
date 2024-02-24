FROM apache/airflow:2.8.0
USER root

# Update package lists, install dependencies, and clean up
RUN apt-get update && apt-get install -y python3-pip 

EXPOSE 8080

# Create a directory inside the container
RUN mkdir -p etl
COPY ./etl ./etl

USER airflow

# Install necessary Python packages
RUN pip install apache-airflow \
    pandas requests 'apache-airflow[amazon]' \
    s3fs bs4 streamlit plotly matplotlib wordcloud
    
# Define the command to run when the container starts
CMD ["airflow standalone"]
