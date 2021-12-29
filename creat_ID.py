# -*- coding: utf-8 -*-
import os
import shutil
 
def listname(path,idtxtpath):
    filelist = os.listdir(path);  # 该文件夹下所有的文件（包括文件夹）
    filelist.sort()
    f = open(idtxtpath, 'w')
    for files in filelist:  # 遍历所有文件
        Olddir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        f.write(Olddir)
        f.write('\n')
    f.close()
 
savepath = '/home/data/zhangxin/NWPU_VHR-10'
print(savepath )
imgidtxttrainpath = savepath+"/train.txt"
imgidtxtvalpath = savepath + "/value.txt"
imgidtxttestpath = savepath + "/test.txt"
listname('/home/data/zhangxin/NWPU_VHR-10/voc_form/train/JPEGImages',imgidtxttrainpath)
listname('/home/data/zhangxin/NWPU_VHR-10/voc_form/val/JPEGImages' ,imgidtxtvalpath)
print("train.txt, value.txt and test.txt have been created!")
