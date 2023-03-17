import numpy as np
import sklearn
import sklearn.linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score

X_train = [["hej", "med", "dig"], ["jeg", "kender", "en", "orm"], ["Min", "hund", "hedder", "Mads"], ["Hvarbehar?"], ["To", "stoddere", "på", "en", "bænk"]]
y_train = [1, 0, 0, 1, 0]

X_test = X_train = [["hej", "med", "dig"], ["jeg", "kender", "en", "orm"], ["Min hund hedder Mads"], ["Hvarbehar?"], ["To stoddere på en bænk"]]
y_test = [1, 0, 0, 1, 0]

modelR = sklearn.linear_model.LogisticRegression(max_iter=2170)
modelR.fit(X_train, y_train)
y_predR = ([x for x in modelR.predict(X_test)])

mseR = mean_squared_error(y_test, y_predR)
accR = accuracy_score(y_test, y_predR)
print(mseR)
print(accR)