from prefect import flow, task
import time

@task(log_prints=True)
def name_task(name):
    print("hello again", name)
    return "hello again"

@task(log_prints=True)
def sleep_task(sleepLength:int=10):
    time.sleep(sleepLength)
    print("slept")
    return "slept"

@flow(log_prints=True)
def sleep_task_flow(name:str="world", sleepLength:int=10):
    '''### Sleep task flow
```python
from prefect import flow, task
from prefect import time

@task(log_prints=True)
def name_task(name):
    print("hello again", name)
    return "hello again"

@task(log_prints=True)
def sleep_task(sleepLength:int=10):
    time.sleep(sleepLength)
    print("slept")
    return "slept"

@flow(log_prints=True)
def sleep_task_flow(name:str="world"sleepLength:int=10):
    name_task()
    print("hello", name)
    return 'hello'
```
    '''
    name_task(name)
    sleep_task(sleepLength)
    print("hello", name)
    return 'hello'


if __name__ == '__main__':
    sleep_task_flow.serve(name='world')