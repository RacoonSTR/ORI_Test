import csv
import json
import os

def read_internal(folder):
    files = []
    filenames = os.listdir(folder + '/markup')
    for filename in filenames:
        with open('/'.join([folder, 'markup', filename]), 'r') as file:
            files.append({'filename': filename, 'markups': json.loads(file.read())})
    return files

def read_internal_csv(folder):
    with open(folder + '/markup.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        rows = list(csvreader)
    return rows

def internal_to_internal_csv(files):
    csv_string = 'filename,width,height,class,xmin,ymin,xmax,ymax'
    for file in files:
        for markup in file['markups']:
            markup_string = ','.join([file['filename'], '999', '999', markup["label"], str(markup['x']), str(markup['y']), str(markup['x1']), str(markup['y1'])])
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