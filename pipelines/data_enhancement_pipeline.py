import pandas as pd
from utils.constants import TRANSFORMED_PATH, OUTPUT_PATH
from etls.data_enhancement_etl import data_enhancement

def enhanced_data(ti):
    input_csv_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')
    output_csv_path = f'{TRANSFORMED_PATH}/transformed_{input_csv_path.split("/")[-1]}'
    data_enhancement(input_csv_path, output_csv_path)
    return output_csv_path