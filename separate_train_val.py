# -*- coding:UTF-8 -*-
import shutil
 

def separate_img(ori_img_path, train_txt, val_txt, train_path, val_path):
    train = open(train_txt, 'r') 
    train = list(train)
    train_path = train_path + '/JPEGImages'
    for name in train:
        name = name.split('/')[-1].split('.')[0]
        name = name + '.jpg'
        shutil.copy(ori_img_path + '/'+ name, train_path)
    val = open(val_txt, 'r') 
    val = list(val)
    val_path = val_path + '/JPEGImages'
    for name in val:
        name = name.split('/')[-1].split('.')[0]
        name = name + '.jpg'
        shutil.copy(ori_img_path +'/'+ name, val_path)

def separate_label(ori_label_path, train_txt, val_txt, train_path, val_path):
    train = open(train_txt, 'r') 
    train = list(train)
    train_path = train_path + '/annotations' 
    for name in train:
        name = name.split('/')[-1].split('.')[0]
        name = name + '.xml'
        shutil.copy(ori_label_path + '/'+ name, train_path)
    val = open(val_txt, 'r') 
    val = list(val)
    val_path = val_path + '/annotations'
    for name in val:
        name = name.split('/')[-1].split('.')[0]
        name = name + '.xml'
        shutil.copy(ori_label_path + '/'+ name, val_path)

ori_img_path = '/home/data/zhangxin/NWPU_VHR-10/voc_form/JPEGImages'
ori_label_path = '/home/data/zhangxin/NWPU_VHR-10/voc_form/annotations'
train_txt = '/home/data/zhangxin/NWPU_VHR-10/voc_form/train.txt'
val_txt = '/home/data/zhangxin/NWPU_VHR-10/voc_form/value.txt'
val_path = '/home/data/zhangxin/NWPU_VHR-10/voc_form/val'
train_path = '/home/data/zhangxin/NWPU_VHR-10/voc_form/train'
separate_img(ori_img_path, train_txt, val_txt, train_path, val_path)
separate_label(ori_label_path, train_txt, val_txt, train_path, val_path)