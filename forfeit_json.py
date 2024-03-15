import csv
import json
from pprint import pprint


def db(file):
    with open(file, encoding='UTF-8') as f:
        json_reader = csv.DictReader(f)
        json_reader = list(json_reader)
        return json_reader

data = db('files/reestr.csv')

def json_write(data):
    with open('files/result.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        print(json_str)


json_write(data)
