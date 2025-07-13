from airflow import DAG
from airflow.operators.python import PythonOperator 
from datetime import timedelta
from datetime import datetime
import subprocess
import os

# Adjust this path to where your scripts live
SCRIPT_DIR = "/opt/airflow/scripts"

def print_welcome():
    print('Welcome to Airflow!')

def print_date():
    print('Today is {}'.format(datetime.today().date()))

# Function to run the data ingestion script
def data_ingestion():
    subprocess.run(["python", os.path.join(SCRIPT_DIR, "00_data_ingestion.py")], check=True)

def data_visualization():
    subprocess.run(["python", os.path.join(SCRIPT_DIR, "01_data_visualization.py")], check=True)


dag = DAG(

    'data_pipeline_dag',

    default_args={'start_date': datetime.now() - timedelta(days=1)},

    schedule='0 23 * * *',

    catchup=False

)



print_welcome_task = PythonOperator(

    task_id='print_welcome',

    python_callable=print_welcome,

    dag=dag

)



print_date_task = PythonOperator(

    task_id='print_date',

    python_callable=print_date,

    dag=dag

)



data_ingestion_task = PythonOperator(
    task_id='data_ingestion',
    python_callable=data_ingestion,
)

data_visualization_task = PythonOperator(
    task_id='data_visualization',
    python_callable=data_visualization,
)



# Set the dependencies between the tasks

print_welcome_task >> print_date_task >> data_ingestion_task >> data_visualization_task