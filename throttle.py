from prefect import flow, task
from prefect.concurrency.sync import rate_limit


@task
def my_task(i):
    return i


@flow
def my_flow():
    for _ in range(50000):
        rate_limit("slow-my-flow", occupy=1)
        my_task.submit(1)


if __name__ == "__main__":
    my_flow()