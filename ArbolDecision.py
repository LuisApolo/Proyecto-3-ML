#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


def load():
    #cargar y leer datos
    df = pd.read_fwf('Data/yeast.data', names = ['sq_name', 'mcg', 'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc', 'class'])
    
    #invocar funcion
    decisionTree(df)


def decisionTree(df):
    #borrar primera columna
    df = df.drop('sq_name', axis = 1)
    

def main():
    load()


if __name__ == "__main__":
    main()
