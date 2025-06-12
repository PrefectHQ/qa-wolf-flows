from prefect import flow
import time

@flow(log_prints=True)
def sub_flow_3():
    print('sleepy sub flow 3')
    return

@flow(log_prints=True)
def sub_flow_2():
    time.sleep(10)
    print('sleep sub flow 2')
    return

@flow(log_prints=True)
def sub_flow_1():
    time.sleep(10)
    print('sleep sub flow 1')
    return

@flow(log_prints=True)
def main_flow():
    print('main sleepy flow')
    sub_flow_1()
    sub_flow_2()
    sub_flow_3()