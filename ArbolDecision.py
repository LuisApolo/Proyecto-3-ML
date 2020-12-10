#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def load():
    #cargar y leer datos
    df = pd.read_fwf('Data/yeast.data', names = ['sq_name', 'mcg', 'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc', 'class'])
    
    #invocar funcion
    decisionTree(df)


def decisionTree(df):
    #borrar primera columna
    df = df.drop('sq_name', axis = 1)
    
    #separar conjuntos de datos
    train, validate, test = np.split(df.sample(frac = 1), [int(.8*len(df)), int(.9*len(df))])
    
    #eliminar columna class de 'y' y X entrenamiento
    y_train = train['class']
    X_train = train.drop('class', axis = 1)
    
    #eliminar columna class de 'y' y X prueba
    y_test = test['class']
    X_test = test.drop('class', axis = 1)
    
    accGini = []
    accEntropy = []
    maxDepth = []
    
    for i in range(1,40):
        model = DecisionTreeClassifier(criterion = "entropy", max_features = "log2", max_depth = i, random_state = 2)
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        acc = accuracy_score(y_test, prediction)
        accEntropy.append(acc)
        
        model = DecisionTreeClassifier(criterion = "gini", max_features = "log2", max_depth = i, random_state = 2)
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        acc = accuracy_score(y_test, prediction)
        accGini.append(acc)
        
    print(accGini)
    

def main():
    load()


if __name__ == "__main__":
    main()
