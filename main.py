from airflow.decorators import dag, task
import pendulum

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
    '''
    using @dag decorator to create our first date pipline
    :return:
    '''
    pass
