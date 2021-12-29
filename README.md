# dataset_format_conversion_for_remote_sensing_object_detection (RSOD)

Data format conversion for object detection

## 常用的目标检测的数据集主流格式
- YOLO 格式 
- VOC 格式
- COCO 格式

### YOLO格式
类别 中心位置x相对坐标 中心位置y相对坐标 框相对宽 框相对长

eg:
```
0 0.6226513569937369 0.6503712871287128 0.06993736951983298 0.11757425742574258
```
### VOC格式
是.xml格式
eg:
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
