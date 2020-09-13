import csv
import os

import common

def to_pascalvoc(source_folder, dest_folder):
    data = read_internalcsv(source_folder)

    files_dict = {}

    for markup in data:
        if markup['filename'] not in files_dict:
            files_dict[markup['filename']] = {'objects': '', **common.get_image_data(source_folder + '/' + markup['filename'])}
        
        files_dict[markup['filename']]['objects'] += get_object_xml(markup) + '\n'
    
    xml_string = ''

    for file_name in files_dict:
        xml_string += get_annotation_xml(file_name, files_dict[file_name])

    common.save_file(xml_string, dest_folder + '/markup.xml')
    common.copy_folder(source_folder + '/images', dest_folder + '/images')

def read_internalcsv(folder):
    with open(folder + '/markup.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        rows = list(csvreader)
    return rows

def get_object_xml(obj):
    with open('templates/pascal_voc_object_template.xml', 'r') as obj_xml:
        return obj_xml.read().format(xmin=obj['xmin'], xmax=obj['xmax'], ymin=obj['ymin'], ymax=obj['ymax'], name=obj['class'])

def get_annotation_xml(file_path, img_data):
    with open('templates/pascal_voc_annotation_template.xml', 'r') as annotation_xml:
        return annotation_xml.read().format(filename=img_data['filename'], path=img_data['path'], objects=img_data['objects'], width=img_data['width'], height=img_data['height'])
