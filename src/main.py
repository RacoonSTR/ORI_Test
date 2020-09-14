import os
import importlib

import internal
import internal_csv
import pascal_voc

# Test variables
FOLDER_1_1 = './data/internal'
FOLDER_1_2 = './result/internal'
FOLDER_2_1 = './data/internalCSV'
FOLDER_2_2 = './result/internalCSV'
FOLDER_2_3 = './result/internalCSV_2'
FOLDER_3_1 = './data/pascalVOC'
FOLDER_3_2 = './result/pascalVOC'

INTERNAL = 'internal'
INTERNAL_CSV = 'internal_csv'
PASCAL_VOC = 'pascal_voc'

#SOURCE_FOLDER = os.environ('SOURCE_FOLDER')
#DEST_FOLDER = os.environ('DEST_FOLDER')
#SOURCE_FORMAT = os.environ('SOURCE_FORMAT')
#DEST_FORMAT = os.environ('DEST_FORMAT')

SOURCE_FORMAT = INTERNAL
DEST_FORMAT = INTERNAL_CSV

def main():
    sourse_module = importlib.import_module(SOURCE_FORMAT)
    if sourse_module is None:
        print("ERROR: Can't find module for source format")
    else:
        convert_method = getattr(sourse_module, 'to_' + DEST_FORMAT, None)
        if convert_method is None:
            print("ERROR: Can't find method for destination format")
        else:
            convert_method(FOLDER_1_1, FOLDER_2_2)

if __name__ == "__main__":
    main()