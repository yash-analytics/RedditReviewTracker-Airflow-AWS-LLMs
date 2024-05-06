import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.data_enhancement_pipeline import enhanced_data

default_args = {
    'owner': 'Yash Joshi',
    'start_date': datetime(2024, 5, 5)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='redditreviewtracker',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'shopify',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

# Data Enhancement
data_enhancement = PythonOperator(
    task_id='enhance',
    python_callable=enhanced_data,
    dag=dag
)

# Upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >>  data_enhancement >> upload_s3