"""module to ingest csv data for the titanic dataset.Code structure imported
from https://docs.python.org/3/library/csv.html"""

import csv
def load_data(filename='train.csv'):
    data={}
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(', '.join(row))
            data[row[0]]=row
    return data

if __name__ == "__main__":
    load_data()
