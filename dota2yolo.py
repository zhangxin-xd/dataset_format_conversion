
import os
from PIL import Image
import numpy as np

imagepath = ""#AOD数据集中PLANE图片所在文件夹
oldpath = ""#AOD数据集中PLANE标签所在文件夹（原标签文件）
newpath = ""#转换后存放yolo格式标签的文件夹

#该数据集中包含的目标类别，按names文件排序
#classes = ["ship","bridge","groundtrackfield","storagetank","basketballcourt","tenniscourt","airplane",\
#           "baseballdiamond","harbor","vehicle","crossroad","T-junction","parkinglot"]
oldlabels = os.listdir(oldpath)
for oldlabel in oldlabels:#遍历原标签文件夹中所每张图片对应的标签文件，逐个处理
    if ('.txt' in oldlabel): #判断是否为标签文件
      with open(oldpath + oldlabel,'r') as f:
          contents = f.readlines()#读取标签文件里的所有行
          fo = open(newpath+oldlabel,"w")#以只写方式创建并打开转换后的标签文件
          fo.truncate()
          img = np.array(Image.open(imagepath+oldlabel.strip('.txt')+'.tiff'))#获取标签文件对应的图片文件
          sh,sw= img.shape[0],img.shape[1] #获取标签对应图片的宽和高，以像素表示
          for content in contents: #逐行操作该标签文件里的内容
              content = content.strip('\n')  #去除字符串末尾的换行符
              content = content.split() #以‘ ’为标志分割字符串
        
              yolo=[]#用列表yolo作为中间变量，将当前这个原始标签文件中的信息转换后，写入新标签文件中
#             i = classes.index(content[8]) #判断该类别所对应的序号
#             yolo.append('i ')
              yolo.append('0 ')#在yolo变量内添加字符'0 ',0  代表类别为PLANE
              
              #对获取的数据进行yolo格式下的转换
              x1 = float(content[0])#x1
              y1 = float(content[1])#y1
              x2 = float(content[2])#x2
              y4 = float(content[7])#y4
              
              w1 = float(x2-x1)
              h1 = float(y4-y1)
              
              w = float(w1/sw)
              h = float(h1/sh)
              x = float((x1+x2)/2/sw)
              y = float((y1+y4)/2/sh)
              
              #将转换后的数据放入yolo变量中
              yolo.append(str(x)+' ')
              yolo.append(str(y)+' ')
              yolo.append(str(w)+' ')
              yolo.append(str(h)+'\n')
              fo.writelines( yolo )#将yolo变量中的所有信息写为新标签文件中的一行
              fo.close
             