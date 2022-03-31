import glob
import os

# img_path = '/home/data/zhangxin/NWPU_VHR-10/dota_form/500/val_split/images'
# label_path = '/home/data/zhangxin/NWPU_VHR-10/dota_form/500/val_split/labelTxt'
img_path = '/home/data/zhangxin/NWPU_VHR-10/500_split/train/images'
label_path = '/home/data/zhangxin/NWPU_VHR-10/500_split/train/annotations'
img_src = glob.glob(img_path + '/*')
label_src = glob.glob(label_path + '/*')
img_name = []

num_img = 0
for img in img_src:
    num_img += 1
    img_basename = os.path.basename(img)
    img_onlyname = os.path.splitext(img_basename)

    img_name.append(img_onlyname[0])
    
print(num_img)
label_name = []

num_label = 0
for label in label_src:
    num_label += 1
    label_basename = os.path.basename(label)
    label_onlyname = os.path.splitext(label_basename)

    label_name.append(label_onlyname[0])
    
print(num_label)
not_in_list = []

for img in img_name:
    if img not in label_name: not_in_list.append(img)

print(len(not_in_list))
print(not_in_list)
path = img_path + not_in_list[0] + ".jpg"
print(path)
# Remove training samples which do not have anotation.

count = 0
for item in not_in_list:
    path = img_path + '/' + item + ".jpg"
    if os.path.exists(path):
        os.remove(path)
        count += 1
    else:
        print("The file does not exist")
        
print(count)