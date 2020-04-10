import json
import csv

csv_file_path = "C:/Users/guyri/Desktop/common/common-voice/cv-valid-dev.csv"
data_json_file_path = "/speechtotext/jasons/data.json"
data_sort = []


def data_to_json():
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
        linecount = 0
        for item in data:
            if linecount == 0:
                linecount+=1
            else:
                data_sort.append({'path':item[0], 'text':item[1]})
                linecount+=1

        print(data_sort)

    with open(dump_json_file_path, 'w') as json_file:
        json_file.write(json.dumps(data_sort, indent=4))


if __name__ == "__main__":
    data_to_json()



"""
TO DO:
Reformat the json file to the correct order as specified in the API for the speech-to-text model
Finish downloading the training data (On PC NOT LAPTOP)
Resolve all conflicting PATH issues

"""