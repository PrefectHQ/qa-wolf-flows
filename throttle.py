from prefect import flow, task
from prefect.concurrency.sync import rate_limit
import time

@task
def my_task(i):
    return i


@flow(log_prints=True)
def sub_flow_1():
    time.sleep(10)
    print('sub flow 1')
    return


@flow
def my_flow():
    for _ in range(50000):
        rate_limit("slow-my-flow", occupy=1)
        my_task.submit(1)


if __name__ == "__main__":
    my_flow()