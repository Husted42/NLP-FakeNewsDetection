import re
import csv
import os
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#Remember to run the line below the first time 
#nltk.download('punkt')

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
''' creates dataframe (Run fuctions) '''
def createDataframe(input): 
    df = pd.read_csv(input)
    df = cleanContent(df, 'content')
    return df

''' Cleans and tokenizes text  '''
def cleanContent(input, columnName): 
    ##### Not tokenized
    input[columnName] = input[columnName].apply(str.lower)
    #regexList contains all the things we want to remove
    regexList = ['for', '\.', '12', ':', '&']
    for elm in regexList:
        input[columnName] = input[columnName].str.replace(elm, '', regex=True)
    
    ##### Tokenized
    stop_words = set(stopwords.words('english'))
    for i in range(0, len(input[columnName])):
        colElm = input.at[i, columnName]
        colElm = nltk.word_tokenize(colElm)
        filteredSentence = []
        for w in colElm:
            if w not in stop_words:
                filteredSentence.append(w)
        filteredSentence = ' '.join(filteredSentence)
        input.at[i, columnName] = filteredSentence
    return input

#Converts to csv File
def run(inp):
    inp = inp.to_csv('redactedNews.csv', index = True)

##### -- Calls -- #####
run(createDataframe(testSample))
print(createDataframe(testSample))
