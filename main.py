import csv
import json
import os

def load_internal(folder):
    files = []
    filenames = os.listdir(folder)
    for filename in filenames:
        with open('/'.join([folder, filename]), 'r') as f:
            files.append({'filename': filename, 'markups': json.loads(f.read())})
    return files


def internal_to_internal_csv(files):
    csv_string = 'filename,width,height,class,xmin,ymin,xmax,ymax\n'
    for file in files:
        for markup in file['markups']:
            markup_string = ','.join([file['filename'], '999', '999', markup["label"], str(markup['x']), str(markup['y']), str(markup['x1']), str(markup['y1'])])
            csv_string += markup_string + '\n'
    return csv_string

def main():
    folder = 'markup/markup'
    print(internal_to_internal_csv(load_internal(folder)))

if __name__ == "__main__":
    main()