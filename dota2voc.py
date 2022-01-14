import os, sys
import glob
from PIL import Image
import argparse

def txtLabel_to_xmlLabel(classes_file,source_txt_path,source_img_path,save_xml_path):
    if not os.path.exists(save_xml_path):
        os.makedirs(save_xml_path)
    classes = open(classes_file).read().splitlines()
    print(classes)
    for file in os.listdir(source_txt_path):
        img_path = os.path.join(source_img_path,file.replace('.txt','.jpg')) #png to jpg
        img_file = Image.open(img_path)
        txt_file = open(os.path.join(source_txt_path,file)).read().splitlines()
        print(txt_file)
        xml_file = open(os.path.join(save_xml_path,file.replace('.txt','.xml')), 'w')
        width, height = img_file.size
        xml_file.write('<annotation>\n')
        xml_file.write('\t<folder>simple</folder>\n')
        xml_file.write('\t<filename>' + str(file) + '</filename>\n')
        xml_file.write('\t<size>\n')
        xml_file.write('\t\t<width>' + str(width) + ' </width>\n')
        xml_file.write('\t\t<height>' + str(height) + '</height>\n')
        xml_file.write('\t\t<depth>' + str(3) + '</depth>\n')
        xml_file.write('\t</size>\n')

        for line in txt_file:
            print(line)
            line_split = line.split(' ')

            xml_file.write('\t<object>\n')
            xml_file.write('\t\t<name>'+ str(line_split[8]) +'</name>\n')
            xml_file.write('\t\t<pose>Unspecified</pose>\n')
            xml_file.write('\t\t<truncated>0</truncated>\n')
            xml_file.write('\t\t<difficult>0</difficult>\n')
            xml_file.write('\t\t<bndbox>\n')
            xml_file.write('\t\t\t<xmin>' + str(line_split[0]) + '</xmin>\n')
            xml_file.write('\t\t\t<ymin>' + str(line_split[1]) + '</ymin>\n')
            xml_file.write('\t\t\t<xmax>' + str(line_split[4]) + '</xmax>\n')
            xml_file.write('\t\t\t<ymax>' + str(line_split[5]) + '</ymax>\n')
            xml_file.write('\t\t</bndbox>\n')
            xml_file.write('\t</object>\n')
        xml_file.write('</annotation>')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--classes_file', type=str, default="/home/data/zhangxin/NWPU_VHR-10/voc_form/classes.txt")
    parser.add_argument('--source_txt_path', type=str, default="/home/data/zhangxin/NWPU_VHR-10/300_split/labelTxt")
    parser.add_argument('--source_img_path', type=str, default="/home/data/zhangxin/NWPU_VHR-10/300_split/images")
    parser.add_argument('--save_xml_path', type=str, default="/home/data/zhangxin/NWPU_VHR-10/300_split/voc/annotations")
    opt = parser.parse_args()

    txtLabel_to_xmlLabel(opt.classes_file,opt.source_txt_path,opt.source_img_path,opt.save_xml_path)
