#!/usr/bin/env python
 
import sys
import censys
from censys import *
 
api = censys.ipv4.CensysIPv4(api_id="API_ID", api_secret="API_SECRET")
 
res = api.search(sys.argv[1])
matches = res['metadata']['count']
pageNum = matches / 100
if matches % 100 != 0:
    pageNum = pageNum + 1
 
count = 1
while count <= pageNum:
    res = api.search(sys.argv[1], page=count)
    count = count+1
    for i in res.get('results'):
        print "{} {}".format(i.get("ip"), " ".join(i.get('protocols'))