from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="run_python_file",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
) as dag:

    run_script_c = BashOperator(
        task_id="customers",
        bash_command="""
            cd /opt/airflow/dags/pipelines
            python customers.py
        """,
    ),

    run_script_p = BashOperator(
        task_id="products",
        bash_command="""
            cd /opt/airflow/dags/pipelines
            python products.py
        """,
    )

    run_script_c >> run_script_p

