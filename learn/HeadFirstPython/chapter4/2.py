#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pickle

with open("mydata.bin", 'wb') as mysavedata:
    pickle.dump([1, 2, 'three'], mysavedata)

