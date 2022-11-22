from datetime import timedelta

import pandas as pd
import sys
from airflow import DAG
from airflow.utils.dates import days_ago

sys.path.append('/home/karencaro/airflow/unit5_logging_airflow')

from unit5_logging_airflow.logging_setup import logger

# defining DAG arguments
default_args = {
 'owner': 'Karen',
 'start_date': days_ago(0),
 'email': ['some@somemail.com'],
 'email_on_failure': False,
 'email_on_retry': False,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}


dag = DAG(
 'unit5',
 default_args=default_args,
 description='My first DAG',
 schedule_interval=timedelta(days=1),
)


# Tasks
@dag.task(task_id="read_top10")
def read_top10() -> None:
    """Process a dataset and returns countries with most medals.
    """

    # Read CSV from web
    url = "http://winterolympicsmedals.com/medals.csv"

    try:
        df = pd.read_csv(url)

        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(ascending=False)
        top_countries.head(10)

        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()

        # Save data frame in Excel format
        to_countries_df.to_excel(
            '/home/karencaro/airflow/dags/unit5_logging_airflow'
            '/results/top10_medals_by_country.xlsx')

        logger.info('...File processed successfully...')

    except BaseException:
        logger.error('...Error when processing file...', exc_info=True)


# Task pipeline
read_top10()
