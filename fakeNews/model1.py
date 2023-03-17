import numpy as np
import sklearn
import sklearn.linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

df_ = pd.read_csv('redactedSample.csv')

def vectorize(inp):
    vectorizer = CountVectorizer()
    n = vectorizer.fit_transform(inp['content'])
    n = n.toarray()
    return n

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

X_train = vectorize(df_)
y_train = binary(df_)

modelR = sklearn.linear_model.LogisticRegression(max_iter=500)
modelR.fit(X_train, y_train)
pred = modelR.predict(X_train)
MSE = mean_squared_error(y_train, pred)
ACC = accuracy_score(y_train, pred)
print("MSE : " + str(MSE))
print("ACC : " + str(ACC) )


# mseR = mean_squared_error(y_test, y_predR)
# accR = accuracy_score(y_test, y_predR)
# print(mseR)
# print(accR)