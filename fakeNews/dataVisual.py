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

def plot(data):
    sort = dict(sorted(wordDic(data).items(), key=lambda x: x[1], reverse=True))
    return sort
print((plot('redactedNews.csv')))


