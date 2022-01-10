# *_*coding: utf-8 *_*
# Author --LiMing--

import os
import random
import shutil
import time

def copyFile(fileDir,labelDir):
    image_list = os.listdir(fileDir) # 获取图片的原始路径
    image_number = len(image_list)
    

    train_number = int(image_number * train_rate)
    train_sample = random.sample(image_list, train_number) # 从image_list中随机获取0.8比例的图像.
    test_sample = list(set(image_list) - set(train_sample))
    sample = [train_sample, test_sample]

    # 复制图像到目标文件夹
    for k in range(len(save_dir)):
        if os.path.isdir(save_dir[k]):
            for name in sample[k]:
                shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k] + name))
                shutil.copy(os.path.join(labelDir, name.replace('.jpg','.xml')), os.path.join(save_dir[k].replace('/images','/annotations') + name.replace('.jpg','.xml')))
        else:
            os.makedirs(save_dir[k])
            for name in sample[k]:
                shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k] + name))
                shutil.copy(os.path.join(labelDir, name.replace('.jpg','.xml')), os.path.join(save_dir[k].replace('/images','/annotations') + name.replace('.jpg','.xml')))
if __name__ == '__main__':
    time_start = time.time()

    # 原始数据集路径
    image_Dir = '/home/data/zhangxin/NWPU_VHR-10/300_split/images/'
    labelDir = '/home/data/zhangxin/NWPU_VHR-10/300_split/voc/annotations/'

    # 保存路径
    save_train_dir = '/home/data/zhangxin/NWPU_VHR-10/300_split/voc/train/images/'
    save_test_dir = '/home/data/zhangxin/NWPU_VHR-10/300_split/voc/val/images/'
    save_dir = [save_train_dir, save_test_dir]

    # 训练集比例
    train_rate = 0.25

    # 数据集类别及数量
    file_list = os.listdir(image_Dir)
    #num_classes = len(file_list)

    #for i in range(num_classes):
    #class_name = file_list[i]
    
    copyFile(image_Dir,labelDir)
    print('%s划分完毕！')

    time_end = time.time()
    print('---------------')
    #print('训练集和测试集划分共耗时%s!' % (time_end - time_start)