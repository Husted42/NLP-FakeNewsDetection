import re
import pandas as pd
import matplotlib.pyplot as plt 
import itertools

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

# def plot(data):
#     sort = dict(sorted(wordDic(data).items(), key=lambda x: x[1], reverse=True))
#     plotDictionary = dict(itertools.islice(sort.items(), 50))
#     axis = plt.figure().add_axes([0,0,1,1])
#     x = list((plotDictionary).keys())
#     y = list((plotDictionary).values())
#     axis.bar(x, y)
#     plt.xticks(rotation = 90)
#     plt.show()

def plot(data):
    sort = dict(sorted(wordDic(data).items(), key=lambda x: x[1], reverse=True))
    plotDictionary = dict(itertools.islice(sort.items(), 50))
    words = list(plotDictionary.keys())
    frequency = list(plotDictionary.values())
    plt.bar(words, frequency)
    plt.xticks(rotation = 90)
    plt.show()
    return frequency

print(plot('redactedNews.csv'))


