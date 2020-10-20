import csv
from deviceinfo import device_name, ios_info


def create_csv():
    with open("/Users/pangyang/pythontest/startup/result/启动时间.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["version", "device", 'duration'])  # 先写入columns_name
        # writer.writerows(li)  # 写入多行用writerows


def write_csv(duration, udid, device_type):
    with open("/Users/pangyang/pythontest/startup/result/启动时间.csv", 'a+') as f:
        csv_write = csv.writer(f)
        if device_type == 0:
            device = device_name(udid)[0]
        else:
            device = ios_info(udid)[0]
        device.append(duration)
        print(device)
        csv_write.writerow(device)

