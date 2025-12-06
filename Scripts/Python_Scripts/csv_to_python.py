import csv
import json


def csv_to_python(csv_file):
    """ Takes CSV file and creates a JSON FILE
        :arg csv_file (String)
        :return none
    """
    try:
        file = open(csv_file)
    except FileNotFoundError:
        print("File Not found")
    else:
        print("Printing file's contents " + file.name)
        print(file.read())
        file.seek(0)
        data = list(csv.DictReader(file))
        try:
            with open('output.json', mode='w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
        except FileExistsError:
            print("Error creating JSON File")
        else:
            print("\n\nJson File Was Created!")

def test_json_file():
    """ Tests the JSON File Recently Created
            :arg None
            :return none
    """
    try:
        file = open('output.json')
    except FileNotFoundError:
        print("File Not found")
    else:
        print("Printing file's contents " + file.name)
        print(file.read())

if __name__ == '__main__':
    """ Main Method
        :arg none
        :return none
    """
    csv_file = input("Paste Name of CSV file to convert: ")
    csv_to_python(csv_file)
    test_json_file()