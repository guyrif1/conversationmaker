import json
import csv

csv_file_path = "C:/Users/guyri/Desktop/common/common-voice/cv-valid-train.csv"
data_json_file_path = "C:/Users/guyri/PycharmProjects/conversationmaker/speechtotext/jasons/data.json"
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
                data_sort.append({'path': "C:/Users/guyri/Desktop/common/common-voice/cv-valid-train/"+item[0], 'text': item[1]})
                linecount+=1

        print(data_sort)

    with open(data_json_file_path, 'w') as json_file:
        json_file.write(json.dumps(data_sort, indent=4))


if __name__ == "__main__":
    data_to_json()

