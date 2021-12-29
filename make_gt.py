import os

from vision.utils.misc import Timer
import matplotlib.pyplot as plt
import cv2
import sys
import numpy as np

timer = Timer()

#用的yolo格式
# label_path = "models/voc-model-labels-orig.txt"
label_path = "/home/data/zhangxin/NWPU_VHR-10/classes.txt"
# --------------- #

class_names = [name.strip() for name in open(label_path).readlines()]
num_classes = len(class_names)


# Detection #
# orig_image = plt.imread('soccer.jpg')
img_path = '/home/data/zhangxin/NWPU_VHR-10/imgs'
#label_path = '/home/data/zhangxin/NWPU_VHR-10/voc_form/val/annotations'
imgs = os.listdir(img_path)
class_names = [name.strip() for name in open(label_path).readlines()]
for img in imgs:
    orig_image = cv2.imread(img_path + '/' + img)
    image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
    h, w, c = image.shape
    color = np.random.uniform(0, 255, size = (15, 3))
    labels = open(img_path.replace('imgs','labels') + '/' + img.replace('.jpg','.txt')).read().splitlines()

    # labels = open().read().splitlines()
    # boxes, labels, probs = predictor.predict(image, 10, 0.4)

    for i in range(len(labels)):
        box = labels[i].split(' ')[1:]
        class_name = class_names[int(labels[i].split(' ')[0])]
        w_b = float(box[2]) * w
        h_b = float(box[3]) * h
        x_b = float(box[0]) * w 
        y_b = float(box[1]) * h 

        i_color = int(labels[i][0])

        cv2.rectangle(orig_image, (int(x_b-0.5*w_b), int(y_b-0.5*h_b)), (int(x_b+0.5*w_b), int(y_b+0.5*h_b)), color[i_color], 2)

        cv2.putText(orig_image, class_name,
                    (int(x_b) - 10, int(y_b) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,  # font scale
                    color[i_color],
                    2)  # line type

    cv2.imwrite('/home/data/zhangxin/NWPU_VHR-10/gt_box/' + img, orig_image)

    print("done!")