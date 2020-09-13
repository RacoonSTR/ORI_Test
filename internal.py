import json
import os
import shutil
from PIL import Image

FOLDER_1 = './internal'
FOLDER_2 = './internalCSV'
FOLDER_3 = './pascalVOC'

def to_internal_csv(source_folder, dest_folder):
    data = read_internal(source_folder)

    csv_string = 'filename,width,height,class,xmin,ymin,xmax,ymax'
    for imgData in data:
        img = Image.open('/'.join([source_folder, 'markup', imgData.filename]))

        for markup in imgData['markups']:
            markup_string = ','.join([ 'images/' + imgData.filename, str(img.size.width), str(img.size.height), markup["label"], str(markup['x']), str(markup['y']), str(markup['x1']), str(markup['y1'])])
            csv_string += '\n' + markup_string

    save_internal_csv(csv_string, FOLDER_2)
    copy_folder(source_folder + '/images', dest_folder + '/images')

def save_internal_csv(csv_string, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w') as file:
        file.write(csv_string)
    return

def copy_folder(source_folder, dest_folder):
    try:
        shutil.copytree(source_folder, dest_folder)
    except Exception as e:
        print('Directory not copied. Error: %s' % e)

def read_internal(folder):
    files = []
    filenames = os.listdir(folder + '/images')

    for filename in filenames:
        with open('/'.join([folder, 'markup', os.path.splitext(filename)[0] + '.json']), 'r') as file:
            files.append({'filename': filename, 'markups': json.loads(file.read())})
    return files
