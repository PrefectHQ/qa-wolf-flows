from prefect import flow, pause_flow_run, task
from prefect.input import RunInput

class UserName(RunInput):
    name: str

@task(log_prints=True)
def get_input():
    user_input = pause_flow_run(
        wait_for_input=UserName
    )
    print(f"Hello, {user_input.name}!")

@flow(log_prints=True)
def interactive_flow():
    '''Interactive flow
```python 
class UserName(RunInput):
    name: str

@task(log_prints=True)
def interactive_flow():
    user_input = pause_flow_run(
        wait_for_input=UserName
    )
    print(f"Hello, {user_input.name}!")
    
@flow(log_prints=True)
def interactive_flow():
    get_input()
    ```
'''
    get_input()
    
