#!/usr/bin/python3
import pickle

with open('donotshare', 'rb') as f:
    o = pickle.load(f)

outstr = ''
for line in o:
    for char,n in line:
        outstr += char*n
    outstr += '\n'
print(outstr)
