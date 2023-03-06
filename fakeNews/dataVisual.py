import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import itertools

def createWordList(input, columnName):
    df = pd.read_csv(input)
    lenght = len(df[columnName])
    for i in range (0, (lenght)):
      elm = df.loc[i].at[columnName]
      print ('element number: ' + str(i))
      print (elm)
      

createWordList('redactedNews.csv', 'content')

def countUniqueWords(filename):
    file = open(filename, 'r')
    read_file = file.read().lower()
    words_in_file = read_file.split()  
    count_map = {}
    for i in words_in_file:
        if i in count_map:
            count_map[i] += 1  
        else:
            count_map[i] = 1
    return count_map  
