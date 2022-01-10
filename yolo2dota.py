

import os
from PIL import Image
import numpy as np

imagepath = "/home/data/zhangxin/NWPU_VHR-10/imgs/" #图片路径
oldpath = "/home/data/zhangxin/NWPU_VHR-10/yolo_form/labels/" # YOLO格式标签路径
newpath = "/home/data/zhangxin/NWPU_VHR-10/dota_form/labels/"# DOTA格式标签路径


classes = ["aeroplane","ship","storage_tank","baseball_diamond","tennis_court","basketball_court","ground_track_field",\
          "harbor","bridge","vehicle"]


oldlabels = os.listdir(oldpath)
for oldlabel in oldlabels:
    if ('.txt' in oldlabel): 
      with open(oldpath + oldlabel,'r') as f:
          contents = f.readlines()
          fo = open(newpath+oldlabel,"w")
          fo.truncate()
          img = np.array(Image.open(imagepath+oldlabel.strip('.txt')+'.jpg'))
          sh,sw= img.shape[0],img.shape[1]
          dota=[]
          dota.append('imagesource:GoogleEarth' + '\n')
          dota.append('gsd:0.1' + '\n' )
          for content in contents:
              content = content.strip('\n') 
              content = content.split() 
        
              cl = classes[int(content[0])]
              x1 = float(content[1]) * sw - float(content[3]) * sw * 0.5
              y1 = float(content[2]) * sh - float(content[4]) * sh * 0.5

              x2 = float(content[1]) * sw + float(content[3]) * sw * 0.5
              y2 = float(content[2]) * sh - float(content[4]) * sh * 0.5

              x3 = float(content[1]) * sw + float(content[3]) * sw * 0.5
              y3 = float(content[2]) * sh + float(content[4]) * sh * 0.5

              x4 = float(content[1]) * sw - float(content[3]) * sw * 0.5
              y4 = float(content[2]) * sh + float(content[4]) * sh * 0.5

              dota.append(str(x1)+' ')
              dota.append(str(y1)+' ')
              dota.append(str(x2)+' ')
              dota.append(str(y2)+' ')
              dota.append(str(x3)+' ')
              dota.append(str(y3)+' ')
              dota.append(str(x4)+' ')
              dota.append(str(y4)+' ')
              dota.append(cl+' ')
              dota.append(str(0)+'\n')
              fo.writelines( dota )
              dota = []
          fo.close
