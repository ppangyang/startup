from PIL import Image
import glob
import os
import shutil
import global_var


def processIMG():
    source_path = global_var.source_dir
    target_path = global_var.target_dir

    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)

    shutil.copytree(source_path, target_path)
    print('复制文件夹完成！')

    img_path = glob.glob(target_path+'/*.jpg')
    for file in img_path:
        im = Image.open(file)
        im.thumbnail((400, 400))
        print(im.format, im.size, im.mode)
        im.save(file)
