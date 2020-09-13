import os
import shutil
from PIL import Image

def save_file(data_string, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w') as file:
        file.write(data_string)
    return

def copy_folder(source_folder, dest_folder):
    try:
        shutil.copytree(source_folder, dest_folder)
    except Exception as e:
        print('Directory not copied. Error: %s' % e)

def get_image_data(image_path):
    img = Image.open(image_path)

    return {
        'filename': os.path.split(image_path)[1],
        'path': os.path.split(image_path)[0],
        'width': img.width,
        'height': img.height,
    }