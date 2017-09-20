#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle

try:
    with open("mydata.bin", 'rb') as myrestoredata:
        a_list = pickle.load(myrestoredata)
    print(a_list)
except IOError as err:
    print("File error: " + str(err))
