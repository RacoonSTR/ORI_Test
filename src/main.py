import os
import importlib

FORMATS = {
    'INTERNAL': 'internal',
    'INTERNAL_CSV': 'internal_csv',
    'PASCAL_VOC': 'pascal_voc'
}

SOURCE_FOLDER = os.environ('SOURCE_FOLDER')
DEST_FOLDER = os.environ('DEST_FOLDER')
SOURCE_FORMAT = os.environ('SOURCE_FORMAT')
DEST_FORMAT = os.environ('DEST_FORMAT')

def main():
    try:
        sourse_module = importlib.import_module(SOURCE_FORMAT)
    except ModuleNotFoundError:
        print("ERROR: Can't find module for source format\nAvailable formats:")
        for format in FORMATS:
            print(' - {}'.format(FORMATS[format]))
        return

    convert_method = getattr(sourse_module, 'to_' + DEST_FORMAT, None)
    if convert_method is None:
        print("ERROR: Can't find method for destination format")
    else:
        convert_method(SOURCE_FOLDER, DEST_FOLDER)

if __name__ == "__main__":
    main()