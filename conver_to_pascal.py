# -*- coding: utf-8 -*-

import os
import sys
import xml.etree.cElementTree as ET
import xml.dom.minidom

def parse_line(line):
    line = line.decode("ascii")
    num_part = line.replace("\n","").replace(" ", "").split(":")[1]
    min_part = num_part.split("-")[0]
    max_part = num_part.split("-")[1]

    min_list = min_part.replace("(","").replace(")", "").split(",")
    max_list = max_part.replace("(","").replace(")", "").split(",")
    minx = int(min_list[0])
    miny = int(min_list[1])
    maxx = int(max_list[0])
    maxy = int(max_list[1])
    print(num_part, min_part, max_part, min_list, max_list)
    return (minx, miny, maxx, maxy)


def conver_to_pascal(anno_file):
    file_name = anno_file

    annotation = ET.Element("annotation")
    folder = ET.SubElement(annotation, "folder").text = "kiktech2018"
    filename  = ET.SubElement(annotation, "filename").text = os.path.basename(file_name).replace("json", "jpg")

    with open(anno_file, 'rb') as f:
        for line in f.readlines():
            #only handle boundings
            if b"Bounding" not in line:
                continue

            data = parse_line(line)
            print(data)

        #information from the shape
            label = "person"
            xmin = data[0]
            ymin = data[1]
            xmax = data[2]
            ymax = data[3]

            #
            object = ET.SubElement(annotation, "object")
            name = ET.SubElement(object, "name").text = label
            difficult = ET.SubElement(object, "difficult").text = "0"
            bndbox = ET.SubElement(object, "bndbox")

            #Modify by Minming, the bounding box should always start with 1, and the maximum must small than width
            xminxml = ET.SubElement(bndbox, "xmin").text = str(xmin + 1)
            yminxml = ET.SubElement(bndbox, "ymin").text = str(ymin + 1)
            xmaxxml = ET.SubElement(bndbox, "xmax").text = str(xmax)
            ymaxxml = ET.SubElement(bndbox, "ymax").text = str(ymax)

            print(label)
            print([xmin, ymin], [xmax, ymax])
            print(file_name)
            assert xmax > xmin
            assert ymax > ymin

    tree = ET.ElementTree(annotation)
    xml_filepath = os.path.join(file_name.replace("annotations","PascalAnnotations").replace("txt","xml"))
    tree.write(xml_filepath)


    xml_content = xml.dom.minidom.parse(xml_filepath)  # or xml.dom.minidom.parseString(xml_string)
    pretty_xml_as_string = xml_content.toprettyxml()
    print(pretty_xml_as_string)
    with open(xml_filepath, "w") as f:
        f.write(pretty_xml_as_string)


if __name__ == '__main__':


    count = 0
    with open("Train/annotations.lst") as f:
        for filename in f.readlines():
            count +=  1
            filename = filename.replace("\n", "")
            print(filename)
            conver_to_pascal(filename)

            print(count)

