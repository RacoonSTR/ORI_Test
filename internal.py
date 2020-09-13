import json
import os
from PIL import Image

import common

def to_internal_csv(source_folder, dest_folder):
    data = read_internal(source_folder)

    csv_string = 'filename,width,height,class,xmin,ymin,xmax,ymax'
    for img_data in data:
        img = common.get_image_data('/'.join([source_folder, 'images', img_data['filename']]))

        for markup in img_data['markups']:
            markup_string = ','.join([ 'images/' + img['filename'], str(img['width']), str(img['height']), markup["label"], str(markup['x']), str(markup['y']), str(markup['x1']), str(markup['y1'])])
            csv_string += '\n' + markup_string

    common.save_file(csv_string, dest_folder + '/markup.csv')
    common.copy_folder(source_folder + '/images', dest_folder + '/images')

def read_internal(folder):
    files = []
    filenames = os.listdir(folder + '/images')

    for filename in filenames:
        with open('/'.join([folder, 'markup', os.path.splitext(filename)[0] + '.json']), 'r') as file:
            files.append({'filename': filename, 'markups': json.loads(file.read())})
    return files
