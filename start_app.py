from airtest_app import start
from airtest.core.api import *
import global_var
import time
import threading



class AppStartThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name


    def run(self):
        print("开始线程：启动App" + self.name)
        # 启动app
        start()
        sleep(5)
        print("app启动完成")
        print("退出线程：启动App结束" + self.name)
        time.sleep(5)
        global_var.exitFlag = 0

