# Reddit Review Tracker

## Project Description

**Sector**:
- SaaS (Software as a Service)

**Technologies Used**:
- **Apache Airflow & Celery**: Orchestrates data extraction, transformation, and load (ETL) processes through directed acyclic graphs (DAGs). Three Python operators are defined in [pipelines](./pipelines) which call detailed functions from the [ETLs folder](./etls).
- **Python**: Primary programming language.
- **AWS Services (S3, Glue, Athena, Redshift)**: Used for data storage, processing, and analysis.
- **OpenAI API with Instructor and Pydantic**: Enhances extracted data by categorizing post titles and analyzing sentiments.

**Objective/Goal**:
- To automate insights into customer discussions on platforms like Reddit, adaptable to any subreddit or customer discussion forum.

## Data Source, Transformation & Output

**Data Sources**:
- Extracted from the Reddit API, initially focused on r/shopify.

**Transformation Steps**:
- **Data Extraction**: Managed by `reddit_pipeline` in [pipelines folder](./pipelines/reddit_pipeline.py).
- **Data Enhancement**: Uses `data_enhancement` in [pipelines folder](./pipelines/data_enhancement_pipeline.py), applying sentiment and category analysis via the OpenAI API.
- **Data Storage**: Enhanced data is stored in AWS S3, then processed in AWS Glue and Athena, and loaded into Amazon Redshift.

**Output**: 
- Visualized in Amazon QuickSight. The visual outputs can be viewed in the [Project Screenshots folder](./Project%20Screenshots).

### Deployment and Execution

- **Airflow DAG**: Configured in the [dags folder](./dags), orchestrates the workflow daily. See the DAG run here: ![Airflow DAG Run](./Project%20Screenshots/2.%20Airflow%20DAG%20Run.png)

### QuickSight Visualizations

- **Dashboard Overview**: Provides interactive visualizations of the data. Example dashboard: ![QuickSight Dashboard](./Project%20Screenshots/5.%20QuickSight%20Dashboard.png)

## Additional Visualizations and Insights

- **Docker Setup**: Ensures consistent deployments. Docker build process: ![Docker Build](./Project%20Screenshots/1.%20Docker%20Build.png)
- **AWS S3 Storage**: Critical for data storage, setup visible here: ![S3 Storage](./Project%20Screenshots/3.%20S3.png)
- **Redshift Query Performance**: Illustrated here: ![Redshift Query](./Project%20Screenshots/4.%20Redshift%20Query.png)

## Results

- Automates monitoring and analysis of customer discussions, providing timely insights into sentiments and trends.

## Learnings

- Key learnings include integration of AWS services with Apache Airflow to create a robust automated data pipeline, and using OpenAI's API for data enhancement.