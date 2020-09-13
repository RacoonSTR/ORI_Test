from xml.dom import minidom

import common

def to_internal_csv(source_folder, dest_folder):
    csv_string = 'filename,width,height,class,xmin,ymin,xmax,ymax'

    markup_file = minidom.parse(source_folder + '/markup.xml')
    annotations = markup_file.getElementsByTagName('annotation')
    
    for annotation in annotations:
        filename = annotation.getElementsByTagName('filename')[0].firstChild.nodeValue
        size = annotation.getElementsByTagName('size')[0]
        width = size.getElementsByTagName('width')[0].firstChild.nodeValue
        height = size.getElementsByTagName('height')[0].firstChild.nodeValue
        objs = annotation.getElementsByTagName('object')
        for obj in objs:
            name = obj.getElementsByTagName('name')[0].firstChild.nodeValue
            bndbox = obj.getElementsByTagName('bndbox')[0]
            xmin = bndbox.getElementsByTagName('xmin')[0].firstChild.nodeValue
            ymin = bndbox.getElementsByTagName('ymin')[0].firstChild.nodeValue
            xmax = bndbox.getElementsByTagName('xmax')[0].firstChild.nodeValue
            ymax = bndbox.getElementsByTagName('ymax')[0].firstChild.nodeValue
            markup_string = ','.join(['images/' + filename, width, height, name, xmin, ymin, xmax, ymax])
            csv_string += '\n' + markup_string

    common.save_file(csv_string, dest_folder + '/markup.csv')
    common.copy_folder(source_folder + '/images', dest_folder + '/images')