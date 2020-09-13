import os

import internal
import internal_csv

# Test variables
FOLDER_1_1 = './data/internal'
FOLDER_1_2 = './result/internal'
FOLDER_2_1 = './data/internalCSV'
FOLDER_2_2 = './result/internalCSV'
FOLDER_3_1 = './data/pascalVOC'
FOLDER_3_2 = './result/pascalVOC'

SOURCE_FOLDER = os.environ('SOURCE_FOLDER')
DEST_FOLDER = os.environ('DEST_FOLDER')
SOURCE_FORMAT = os.environ('SOURCE_FORMAT')
DEST_FORMAT = os.environ('DEST_FORMAT')

def main():
    internal.to_internal_csv(FOLDER_1_1, FOLDER_2_2)
    internal_csv.to_pascalvoc(FOLDER_2_1, FOLDER_3_2)

if __name__ == "__main__":
    main()