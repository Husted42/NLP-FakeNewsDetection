import re
import csv
import os

testSample = 'news_sample.csv'

def findDic():
    print(os.getcwd())
    (os.chdir(r'dataScience\fakeNews'))
    print(os.getcwd())
    print(os.listdir())

def getCsv(inp):
    with open(inp, 'r') as input_file, open('redactedSample.csv','w', newline = '') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)
        for row in csv_reader:
            new_row = [cell.lower() for cell in row]
            csv_writer.writerow(new_row)

findDic()
getCsv(testSample)