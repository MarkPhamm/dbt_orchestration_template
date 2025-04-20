import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn", 
    )
)

dbt_snowflake_dag = DbtDag(
    your_project_name = "dbt",
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/{your_project_name}"),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    schedule_interval="@daily",
    start_date=datetime(2024, 9, 10),
    catchup=False,
    dag_id="your_dag_id",
)

dag = dbt_snowflake_dag