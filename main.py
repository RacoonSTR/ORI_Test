import csv
import json
import os

def load_internal(folder):
    files = []
    filenames = os.listdir(folder)
    for filename in filenames:
        with open('/'.join([folder, filename]), 'r') as file:
            files.append({'filename': filename, 'markups': json.loads(file.read())})
    return files

def internal_to_internal_csv(files):
    csv_string = 'filename,width,height,class,xmin,ymin,xmax,ymax'
    for file in files:
        for markup in file['markups']:
            markup_string = ','.join([file['filename'], '999', '999', markup["label"], str(markup['x']), str(markup['y']), str(markup['x1']), str(markup['y1'])])
            csv_string += '\n' + markup_string
    return csv_string

def save_internal_csv(csv_string, path):
    with open(path, 'w') as file:
        file.write(csv_string)
    return

def main():
    folder = 'markup/markup'
    path = 'result/markup.csv'
    save_internal_csv(internal_to_internal_csv(load_internal(folder)), path)

if __name__ == "__main__":
    main()