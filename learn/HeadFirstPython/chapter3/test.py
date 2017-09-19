#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    data = open("missing")
    print(data.readline(), end="")
except IOError:
    print("File error")
finally:
    if 'data' in locals():
        data.close()