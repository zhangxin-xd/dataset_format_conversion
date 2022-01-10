# dataset_format_conversion_for_remote_sensing_object_detection (RSOD)

Data format conversion for object detection

## 常用的目标检测的数据集主流格式
- YOLO 格式 
类别 中心位置x相对坐标 中心位置y相对坐标 框相对宽 框相对长
```
0 0.6226513569937369 0.6503712871287128 0.06993736951983298 0.11757425742574258
```
- VOC 格式
是.xml格式
```
<annotation>
	<folder>simple</folder>
	<filename>001.txt</filename>
	<size>
		<width>958 </width>
		<height>808</height>
		<depth>3</depth>
	</size>
	<object>
		<name>aeroplane</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>562</xmin>
			<ymin>478</ymin>
			<xmax>629</xmax>
			<ymax>573</ymax>
		</bndbox>
	</object>
</annotation>
```
- COCO 格式
## 常用的遥感目标检测的数据集主流格式
- nwpu 数据集
左上位置x,y 右下位置x,y 类别
```
(563,478),(630,573),1 
```
- DOTA 数据集
![d29af925102f4de7c04c6f7618be942](https://user-images.githubusercontent.com/70151784/148685177-2f2c9a97-0cbe-427d-b152-d56587580713.png)
## YOLO格式转换为VOC格式
```
python yolo2voc.py
```
## 将nwpu格式转换为YOLO格式
```
python nwpu2yolo.py
```
## DOTA格式和YOLO格式互相转换
```
python dota2yolo.py
```
```
python yolo2dota.py
```
## DOTA格式转换为VOC格式
```
python dota2voc.py
```
## 遍历文件夹下文件，记录路径
```
creat_ID.py
```
## 分训练验证集
已经有train.txt和val.txt
```
separate_train_val.py
```
没有train.txt和val.txt
```
separate_train_val_no.py
```
## 画ground truth框
```
python make_gt.py
```
