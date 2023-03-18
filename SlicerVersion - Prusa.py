#!/usr/bin/python3

import sys

sourcefile = sys.argv[1]

with open(sourcefile, mode='r', encoding='UTF-8') as fopen:
    data = fopen.readline()
    print(data)
    objNewLine = data
    objNewLine = objNewLine.split("by")[1]
    objNewLine = objNewLine.split("on")[0]
    print(objNewLine)

    seq = "; slicer_version = "+ objNewLine[1:] + "\n;"
    
with open(sourcefile, mode='a', encoding='UTF-8') as fopen:        
    fopen.write(seq)
    
