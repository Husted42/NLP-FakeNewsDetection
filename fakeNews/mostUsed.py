##### -- Imports -- #####
import matplotlib.pyplot as plt 

##### -- Functions -- #####
'''Count words'''
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


'''Filters the top 50 and returns a list'''
def plot(data):
    sort = dict(sorted(wordDic(data).items(), key=lambda x: x[1], reverse=True))
    return sort

##### -- Calls -- #####
print((plot('redactedNews.csv')))


