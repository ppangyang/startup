import os
import re


def device_name(udid):
    value = os.popen("adb devices")

    device = []

    for v in value.readlines():
        android = []
        s_value = str(v).replace("\n", "").replace("\t", "")
        if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
            # udid = s_value[:s_value.find('device')].strip()
            d = os.popen('adb -s {} shell getprop ro.build.version.release'.format(udid))
            deviceAndroidVersion = list(d.readlines())
            android.append("Android " + re.findall(r'^\w*\b', deviceAndroidVersion[0])[0])
            d.close()
            n = os.popen("adb -s {}  -d shell getprop ro.product.model".format(udid))
            devicename = n.readlines()
            android.append(devicename[0].replace("\n", ""))
            n.close()
            device.append(android)
    value.close()
    return device


def ios_info(udid):
    value = os.popen("instruments -s devices")
    device = []
    for v in value.readlines():

        iOS = []

        s_value = str(v).replace("\n", "").replace("\t", "").replace(" ", "")
        print(s_value)
        if v.rfind('Simulator') != -1:
            continue
        if v.rfind("(") == -1:
            continue
        if v.rfind(udid) == -1:
            continue
        iOS.append(re.compile(r'\((.*)\)').findall(s_value)[0])
        print(re.compile(r'\((.*)\)').findall(s_value))
        n = os.popen('ideviceinfo -u "{}" -k ProductType'.format(udid))
        name = list(n.readlines())
        devicename = "/n".join(name).strip('\n')
        iOS.append(phone_type(devicename))
        n.close()
        device.append(iOS)
    return device


def get_udid():
    value = os.popen("adb devices")

    device = []
    for v in value.readlines():
        s_value = str(v).replace("\n", "").replace("\t", "")
        if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
            udid = s_value[:s_value.find('device')].strip()
            device.append(udid)
    value.close()
    return device


# iPhone设备型号转换
def phone_type(producttype):
    if producttype == "iPhone3,1":
        return "iPhone 4"
    elif producttype == "iPhone3,2":
        return "iPhone 4"
    elif producttype == "iPhone3,3":
        return "iPhone 4"
    elif producttype == "iPhone4,1":
        return "iPhone 4S"
    elif producttype == "iPhone5,1":
        return "iPhone 5"
    elif producttype == "iPhone5,2":
        return "iPhone 5"
    elif producttype == "iPhone5,3":
        return "iPhone 5C"
    elif producttype == "iPhone5,4":
        return "iPhone 5C"
    elif producttype == "iPhone6,1":
        return "iPhone 5S"
    elif producttype == "iPhone6,2":
        return "iPhone 5S"
    elif producttype == "iPhone7,1":
        return "iPhone 6 Plus"
    elif producttype == "iPhone7,2":
        return "iPhone 6"
    elif producttype == "iPhone8,1":
        return "iPhone 6S"
    elif producttype == "iPhone8,2":
        return "iPhone 6S Plus"
    elif producttype == "iPhone8,4":
        return "iPhone SE"
    elif producttype == "iPhone9,1":
        return "iPhone 7"
    elif producttype == "iPhone9,2":
        return "iPhone 7 Plus"
    elif producttype == "iPhone10,1":
        return "iPhone 8"
    elif producttype == "iPhone10,2":
        return "iPhone 8 Plus"
    elif producttype == "iPhone10,3":
        return "iPhone X"
    elif producttype == "iPhone10,4":
        return "iPhone 8"
    elif producttype == "iPhone10,5":
        return "iPhone 8 Plus"
    elif producttype == "iPhone10,6":
        return "iPhone X"
    elif producttype == "iPhone11,2":
        return "iPhone XS"
    elif producttype == "iPhone11,4":
        return "iPhone XS Max"
    elif producttype == "iPhone11,6":
        return "iPhone XS Max"
    elif producttype == "iPhone11,8":
        return "iPhone XR"
    elif producttype == "iPhone12,1":
        return "iPhone 11"
    else:
        return None

