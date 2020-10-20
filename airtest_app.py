from airtest.core.api import *


def start():
    init_device("Android")

    connect_device("android:///")

    # devs = device()

    # print(devs.list_app(third_only=True))

    start_app('com.hupu.games')

    sleep(3)

def close():
    stop_app('com.hupu.games')