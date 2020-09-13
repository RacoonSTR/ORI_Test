import csv

def read_internal_csv(folder):
    with open(folder + '/markup.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        rows = list(csvreader)
    return rows

