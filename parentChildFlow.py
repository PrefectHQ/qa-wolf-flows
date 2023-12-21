from prefect import flow

@flow(log_prints=True)
def sub_flow_3():
    print('sub flow 3')
    return

@flow(log_prints=True)
def sub_flow_2():
    print('sub flow 2')
    return

@flow(log_prints=True)
def sub_flow_1():
    print('sub flow 1')
    return

@flow(log_prints=True)
def main_flow():
    print('main flow')
    sub_flow_1()
    sub_flow_2()
    sub_flow_3()