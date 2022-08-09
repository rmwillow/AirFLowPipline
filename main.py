from airflow.decorators import dag, task
import pendulum
import requests
import json

"""dag is for define pipeline and task is how we 
define each task in pipline, pedelum is built off of 
datetime and we get our start, run and end time ofr tasks """


@dag(
    dag_id='data_summary',
    schedule_interval='@daily',
    start_date=pendulum.datetime(2022, 7, 29),
    catchup=False
)
def data_summary():
    """
    using @dag decorator to create our first date pipline
    data_summary will contain all the logic of our data
    :return:
    """
    # first task in pipeline using task decorator
    # - this allows us to write a function to be used as an airflow task (easier way to create an operator)
    # using task flow api which is introduced in airflow 2
    @task()
    def get_data():
        response = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
        print(response.json())



    # when this is called it will initialize the data pipline in airflow
    clean_data = data_summary()
