from record_img import CapThread
from start_app import AppStartThread
import process_img
import get_boot_time
import device_info
import os
import shutil
import global_var
import airtest_app

times = 0

while times < 11:
    target_dir = global_var.target_dir
    source_dir = global_var.source_dir

    # 每次删除文件夹再重新创建此文件夹
    shutil.rmtree(source_dir)
    os.mkdir(source_dir)

    # 创建新线程-启动App并且开启录屏
    thread1 = CapThread(1, "cap")
    thread2 = AppStartThread(2, "appstart")

    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")

    process_img.processIMG()

    filelist = os.listdir(target_dir)  # 获取该目录下的所有文件名
    filelist.sort()

    start_time = get_boot_time.get_start_time(filelist)
    end_time = get_boot_time.get_end_time(filelist, target_dir)

    boot_time = end_time - start_time
    print("启动时间（ms）:" + str(boot_time))

    # 获取手机型号
    n = os.popen("adb shell getprop ro.product.model")
    devicename = n.readlines()

    # device_info.create_csv()
    device_info.write_csv("7.5.21", devicename[0], boot_time)

    global_var.exitFlag = 1
    airtest_app.close()

    times = times + 1
