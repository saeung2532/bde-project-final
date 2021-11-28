from datetime import datetime, time

from airflow import DAG
from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.python import PythonOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

import requests
import json

default_args = {
    'start_date': datetime(2021, 1, 1)
}

def get_covid19_report_today():
    url = 'https://covid19.ddc.moph.go.th/api/Cases/today-cases-all'
    response = requests.get(url)
    data = response.json()

    with open('data.json', 'w') as f:
        json.dump(data, f)

    return data

def select_data():
    hook = MySqlHook("mysql_default")
    sql = """ 
    SELECT * FROM `covidtoday`
    """
    df = hook.get_pandas_df(sql)

    print(df)

def insert_data():
    with open('data.json') as f:
        data = json.load(f)[0]

    print(data) 
    hook = MySqlHook('mysql_default')
    
    sql = """
    INSERT INTO `covidtoday`(`country`, `txn_date`, `new_case`, `total_case`, `new_case_exclude`, `total_case_exclude`, `new_death`, `total_death`, `new_recovered`, `total_recovered`, `update_date`) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    hook.run(sql, parameters=('TH',
                                    data['txn_date'],
                                    int(data['new_case']),
                                    int(data['total_case']),
                                    int(data['new_case_excludeabroad']),
                                    int(data['total_case_excludeabroad']),
                                    int(data['new_death']),
                                    int(data['total_death']),
                                    int(data['new_recovered']),
                                    int(data['total_recovered']),
                                    data['update_date'],
                                    ))

with DAG('covid19_daily',
         schedule_interval='@daily',
         default_args=default_args,
         description='A simple data pipeline for COVID-19 report',
         catchup=False) as dag:
	
    t1 = PythonOperator(
        task_id='get_covid19_report_today',
        python_callable=get_covid19_report_today
    )

    t2 = PythonOperator(
        task_id='select_data',
        python_callable=select_data
    )

    t3 = PythonOperator(
        task_id='insert_data',
        python_callable=insert_data
    )

    t1 >> t3 >> t2 
