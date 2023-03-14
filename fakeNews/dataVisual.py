import re
import pandas as pd
import matplotlib.pyplot as plt 
import itertools

#Dictionary of words
def wordDic(data):
    file = open(data, 'r',  errors="surrogateescape")
    read = file.read().lower()
    words = read.split()  
    dictionary = {}
    for i in words:
        if i in dictionary:
            dictionary[i] += 1  
        else:
            dictionary[i] = 1
    return dictionary  

##### -- 100 most frequent words -- #####
'''Dic of 100 most used words overall'''
def words(data):
    sort = dict(sorted(wordDic(data).items(), key=lambda x: x[1], reverse=True))
    words = dict(itertools.islice(sort.items(), 100))
    return words
#print(words('redactedNews.csv'))

##### -- Plot 10000 most used words -- #####
'''Plots most used words'''
def plot(data, number):
    sort = dict(sorted(wordDic(data).items(), key=lambda x: x[1], reverse=True))
    plotDictionary = dict(itertools.islice(sort.items(), number))
    words = list(plotDictionary.keys())
    frequency = list(plotDictionary.values())
    plt.bar(words, frequency)
    plt.xticks(rotation = 90)
    plt.show()
#plot('redactedNews.csv', 10000)

##### -- data from specefic category -- #####
'''creates a string of all the words in a certain category of 'content''''
def contentToString(input, category):
    df = pd.read_csv(input)
    string = ""
    for i in range(0, len(df.loc[df['type'] == category, 'content'])):
        elm = df.loc[df['type'] == category, 'content'].iloc[i]
        string = string + elm
    return string
#print(contentToString('redactedNews.csv')[0])

'''Counts most used words of String'''
def wordCount(inp):
    words = inp.split()  
    dictionary = {}
    for i in words:
        if i in dictionary:
            dictionary[i] += 1  
        else:
            dictionary[i] = 1
    return(dictionary)
#print(wordCount(contentToString('redactedNews.csv')[0]))

'''Prints most searched words '''
def plot2(inp):
    sort = dict(sorted(inp.items(), key=lambda x: x[1], reverse=True))
    plotDictionary = dict(itertools.islice(sort.items(), 50))
    words = list(plotDictionary.keys())
    frequency = list(plotDictionary.values())
    plt.bar(words, frequency)
    plt.xticks(rotation = 90)
    plt.show()
plot2(wordCount(contentToString('redactedNews.csv', "reliable")))





