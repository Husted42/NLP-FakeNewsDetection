##### -- Imports -- #####
import re
import csv
import os
import pandas as pd
import nltk
import cleantext
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Remember to run the line below the first time 
#nltk.download('punkt')

##### -- Global variables -- #####
testSample = 'readyCsv.csv'

##### -- Functions -- #####
def findDic():
    print(os.getcwd())
    #(os.chdir(r'dataScience\fakeNews'))
    print(os.getcwd())
    print(os.listdir())

def getCsv(inp):
    with open(inp, 'r') as input_file, open('redactedSample.csv','w', newline = '') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)
        for row in csv_reader:
            new_row = [cell.lower() for cell in row]
            csv_writer.writerow(new_row)

''' Creates dataframe (Run fuctions) '''
def createDataframe(input): 
    df = pd.read_csv(input)
    df = cleanContent(df, 'content')
    return df

''' Cleans and tokenizes text  '''
def cleanContent(input, columnName): 
    ##### Not tokenized
    input[columnName] = input[columnName].apply(str.lower)
    #regexList contains all the things we want to remove
    regexList = ['\.', ':', '&', '\,','?',' us ','!',';','$','%','.', '(', ')', '[', ']']
    regexList2 = ['the', 'for', 'one','like','would','time','also','said','many','next','even','could','think','way','may','see','two','first','make', 'get','things','take','years','much']
    regexList2 = regexList2 + ['a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'of', 'with', 'by', 'to', 'from', 'as', 'at', 'that', 'these', 'those', 'if', 'then', 'else', 'while', 'not', 'no']
    regexTemp = []
    for elm in regexList2:
        elm = r'\b' + elm + r'\b'
        regexTemp.append(elm)
    regexList = regexList + regexTemp
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
        filteredSentence = filteredSentence.encode("ascii", "ignore")
        filteredSentence = filteredSentence.decode()
        input.at[i, columnName] = filteredSentence
    input[columnName] = input[columnName].str.replace(r'\d{1}-\d{3}-\d{3}-\d{4}', '<phone>', regex=True)
    input[columnName] = input[columnName].str.replace(r'(https?:?//\S+)', '<URL>', regex=True)
    input[columnName] = input[columnName].str.replace(r'(http//\S+)', '<URL>', regex=True)
    input[columnName] = input[columnName].str.replace(r'\b\d+\b', '<NUM>', regex=True)
    input[columnName] = input[columnName].str.replace(r"r'\b\w\b\s?'", '', regex=True)
    input[columnName] = input[columnName].str.replace(r"'.", '', regex=True)
    input[columnName] = input[columnName].str.replace(r"'", '', regex=True)
    input[columnName] = input[columnName].str.replace(r"`", '', regex=True)
    input[columnName] = input[columnName].str.replace(r"-", '', regex=True)
    input[columnName] = input[columnName].str.replace(r"\*", '', regex=True)
    input[columnName] = input[columnName].str.replace(r"@", '', regex=True)
    input[columnName] = input[columnName].str.replace(r'\s+', ' ', regex=True)
    print(input)
    return input

'''Converts to csv File'''
def run(inp):
    inp = inp.to_csv('redactedNews.csv', index = True)

##### -- Calls -- #####
run(createDataframe(testSample))
#print(createDataframe(testSample))