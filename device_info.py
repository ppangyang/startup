
import csv


def create_csv():
    with open("/Users/pangyang/pythontest/startup/result/启动时间.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["version", "device", 'duration'])  # 先写入columns_name
        # writer.writerows(li)  # 写入多行用writerows

def write_csv(version, device_name, time):
    with open("/Users/pangyang/pythontest/startup/result/启动时间.csv", 'a+',newline='') as f:
        csv_write = csv.writer(f)
        row=[version,device_name,time]
        csv_write.writerow(row)




