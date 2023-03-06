##### -- Imports -- #####
import os
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('punkt')

##### -- Variables -- #####
testSample = 'news_sample.csv'

##### -- Functions -- #####
''' To see/change path '''
def findDic():
    print(os.getcwd()) #get path
    #(os.chdir(r'dataScience\fakeNews')) #set path
    print(os.getcwd())
    print(os.listdir())

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
        input[columnName] = input[columnName].str.replace(elm, '')
    

    ##### Tokenized
    stop_words = set(stopwords.words('english'))
    for i in range (0, len(input[columnName])):
        colElm = input.at[i, columnName]
        colElm = nltk.word_tokenize(colElm)
        lst = []
        for w in colElm:
            if w not in stop_words:
                lst.append(w)

        input.at[i, columnName] = lst
    return input

#Converts to csv File
def run(inp):
    inp = inp.to_csv('redactedNews.csv', index = True)


##### -- Calls -- #####
run(createDataframe(testSample))
print(createDataframe(testSample))