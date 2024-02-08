from prefect import flow, pause_flow_run
from prefect.input import RunInput

class UserName(RunInput):
    name: str

@flow(log_prints=True)
def interactive_flow():
    '''Interactive flow
```python 
class UserName(RunInput):
    name: str

@flow(log_prints=True)
def interactive_flow():
    user_input = pause_flow_run(
        wait_for_input=UserName
    )
    print(f"Hello, {user_input.name}!")```
'''
    user_input = pause_flow_run(
        wait_for_input=UserName
    )
    print(f"Hello, {user_input.name}!")
