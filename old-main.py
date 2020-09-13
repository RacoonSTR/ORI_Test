import csv
import json
import os
import shutil
from PIL import Image

FOLDER_1 = 'internal'
FOLDER_2 = 'internalCSV'
FOLDER_3 = 'pascalVOC'

def copy_folder(source_folder, dest_folder):
    try:
        shutil.copytree(source_folder, dest_folder)
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def read_internal(folder):
    files = []
    filenames = os.listdir(folder + '/images')
    for filename in filenames:
        with open('/'.join([folder, 'markup', os.path.splitext(filename)[0] + '.json']), 'r') as file:
            files.append({'filename': filename, 'markups': json.loads(file.read())})
    return files

def read_internal_csv(folder):
    with open(folder + '/markup.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        rows = list(csvreader)
    return rows

def internal_to_internal_csv(files):
    csv_string = 'filename,width,height,class,xmin,ymin,xmax,ymax'
    for fileData in files:
        file = Image.open('/'.join([folder, 'markup', filename]))

        for markup in fileData['markups']:
            markup_string = ','.join([ 'images/' + file['filename'], str(file.size.width), str(file.size.height), markup["label"], str(markup['x']), str(markup['y']), str(markup['x1']), str(markup['y1'])])
            csv_string += '\n' + markup_string
    return csv_string

def save_internal_csv(csv_string, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w') as file:
        file.write(csv_string)
    return

def main():
    folder = 'markup'
    path = 'result/markup.csv'
    save_internal_csv(internal_to_internal_csv(read_internal(folder)), path)
    read_internal_csv('result')

if __name__ == "__main__":
    main()