import numpy import *
import operator
from os import listdir
import numpy as npy
import pandas as pda
import numpy
def datatoarry(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
