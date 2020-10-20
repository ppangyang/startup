from skimage.metrics import structural_similarity
import numpy as np
import cv2


def compare_picture(picture1, picture2):
    # 读取图片
    img1 = cv2.imread(picture1)
    img2 = cv2.imread(picture2)
    img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
    ssim = structural_similarity(img1, img2, multichannel=True)
    return ssim


def get_start_time(filelist):
    for f in filelist:
        if not f.endswith('.jpg'):
            filelist.remove(f)
        # for item in range(0, len(filelist)):
        #     if filelist[item].endswith('.jpg'):  # 判断图片后缀是否是.jpg
        #         ssim = compare_picture(path + '/' + filelist[item], path + '/' + filelist[item + 1])
        #         if ssim < 0.9:
        #             print(filelist[item + 1])
        #             print(ssim)
        #             start_time = float(filelist[item + 1].replace(".jpg", ""))
        #             break

    print(filelist[0])
    start_time = float(filelist[0].replace(".jpg", ""))
    return start_time


def get_end_time(filelist, target_dir):
    for i in range(len(filelist) - 1, -1, -1):
        if filelist[i].endswith('.jpg'):  # 判断图片后缀是否是.jpg
            ssim = compare_picture(target_dir + '/' + filelist[i], target_dir + '/' + filelist[i - 1])
            if ssim < 0.9:
                print(filelist[i])
                print("ssim:" + str(ssim))
                end_time = float(filelist[i].replace(".jpg", ""))
                break
    return end_time
