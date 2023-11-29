from prefect import flow, task

@task(log_prints=True)
def name_task(name):
    print("hello again", name)
    return "hello again"

@flow(log_prints=True)
def basic_flow(name:str="world"):
    '''### Basic hello world flow
```python
from prefect import flow, task

@task(log_prints=True)
def long_long_long_long_long_name(name):
    print("hello again", name)
    return "hello again"

@flow(log_prints=True)
def basic_flow(name:str="world"):
    long_long_long_long_long_name()
    print("hello", name)
    return 'hello'
```
    '''
    name_task(name)
    print("hello", name)
    return 'hello'

