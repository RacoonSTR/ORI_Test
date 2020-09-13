import internal
import internal_csv

FOLDER_1 = './data/internal'
FOLDER_2 = './data/internalCSV'
FOLDER_3 = './data/pascalVOC'

def main():
    internal.to_internal_csv(FOLDER_1, FOLDER_2)
    internal_csv.to_pascalvoc(FOLDER_2, FOLDER_3)

if __name__ == "__main__":
    main()