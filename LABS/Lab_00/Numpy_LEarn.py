# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:38:13 2019

@author: Rajat_PC
"""
import numpy as np
import time
import sys

SIZE=1000000
L1=list(range(SIZE))
L2=list(range(SIZE))
A1=np.arange(SIZE)
A2=np.arange(SIZE)

start=time.time()

result=[(x,y) for x,y in zip(L1,L2)]

print((time.time()-start)*1000)

start=time.time()
result=A1+A2
print((time.time()-start)*1000)
#print(sys.getsizeof(5)*len(S))

D=np.arange(100)

#print(D.size * D.itemsize)