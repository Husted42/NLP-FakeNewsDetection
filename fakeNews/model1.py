#https://www.youtube.com/watch?v=P47raNuzAW0

!pip install gensim
import numpy as np
import sklearn
import sklearn.linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import gensim
from gensim.models import Word2Vec

import gensim.downloader as api

wv = api.load('word2vec-google-news-300')

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
val = pd.read_csv('val.csv')

'''Copied code from: https://github.com/PradipNichite/Youtube-Tutorials/blob/main/Yotutube_WordVectors.ipynb '''
''' Finds the mean of word vectors '''
def sent_vec(sent):
    vector_size = wv.vector_size
    wv_res = np.zeros(vector_size)
    # print(wv_res)
    ctr = 1
    for w in sent:
        if w in wv:
            ctr += 1
            wv_res += wv[w]
    wv_res = wv_res/ctr
    return wv_res


'''Transform words into vectors'''
def vectorize(inp):
    df = inp
    df['content'] = df['content'].apply(lambda x: x.split())
    df['content'] = df['content'].apply(sent_vec)
    return df['content'].to_list()

'''Helper function for vetorize'''
def check(inp, model):
    if inp in model.wv.key_to_index:
        return model.wv[inp]
    else:
        return None

def binary(inp):
    lst = []
    for i in range(0, (inp.shape[0])):
        colElm = inp.at[i, 'type']
        if colElm == 'fake':
            colElm = 1
        else:
            colElm = 0
        lst.append(colElm)
    return lst


X_train, y_train = vectorize(train), binary(train)
X_test, y_test = vectorize(test), binary(test)
X_val, y_val = vectorize(val), binary(val)
print(X_val)
print(y_val)
print(X_train[1])
print(y_train[1])
print(len(y_train))

print(len(X_val))
print(len(y_val))

#print("------ LINE pred ---------")
#{'C': 100, 'class_weight': None, 'penalty': 'l1', 'solver': 'liblinear'}
modelR = sklearn.linear_model.LogisticRegression(C = 100, class_weight = None, penalty = 'l1', solver='liblinear', max_iter=500 )
modelR.fit(X_train, y_train)
pred = modelR.predict(X_test)
MSE = mean_squared_error(y_test, pred)
ACC = accuracy_score(y_test, pred)
print("MSE : " + str(MSE))
print("ACC : " + str(ACC) )

from sklearn import metrics
predicted = modelR.predict(X_test)
print("Logistic Regression Accuracy:",metrics.accuracy_score(y_test, pred))
print("Logistic Regression Precision:",metrics.precision_score(y_test, pred))
print("Logistic Regression Recall:",metrics.recall_score(y_test, pred))

print(pred.tolist())
print(y_test)
count_ones = 0
count_zeros = 0

# Iterate over the list and increment counters
for num in y_test:
    if num == 1:
        count_ones += 1
    elif num == 0:
        count_zeros += 1

print(f"Number of ones: {count_ones}")
print(f"Number of zeros: {count_zeros}")


from sklearn.model_selection import GridSearchCV

def gridSearch():
    hyperparameters = {
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
        'penalty': ['l1', 'l2', 'elasticnet'],
        'solver': ['liblinear', 'saga'],
        'class_weight': ['balanced', None],
    }
    model = sklearn.linear_model.LogisticRegression()
    grid_search = GridSearchCV(model, hyperparameters, cv=5)
    grid_search.fit(X_test, y_test)

    print("Best hyperparameters: ", grid_search.best_params_)
    print("Test score: ", grid_search.score(X_val, y_val))
#gridSearch()