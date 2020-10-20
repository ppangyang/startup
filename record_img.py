from airtest.core.android.android import ADB, Javacap
import os, time

import threading
import global_var





class CapThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def cap(self):
        adb = ADB()
        devices = adb.devices()
        if not devices:
            raise RuntimeError("At lease one adb device required")
        adb.serialno = devices[0][0]
        javacap = Javacap(adb)
        while global_var.exitFlag:
            frame = javacap.get_frame_from_stream()
            times = int(round(time.time() * 1000))
            file_name = global_var.source_dir + '/' + str(times) + '.jpg'
            with open(file_name, "wb") as f:
                f.seek(0)
                f.truncate()
                f.write(frame)

    def run(self):
        print("开始线程：录屏" + self.name)
        self.cap()
        print("退出线程：录屏" + self.name)



