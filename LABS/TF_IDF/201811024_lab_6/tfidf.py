# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:16:01 2019

@author: Rajat_PC
"""
from collections import Counter  
import re
import numpy as np

D=[]  
A=[]
filename='Try__D.txt'

lookup1 = '<TEXT>'
lookup2='</TEXT>'
# Taking the number of line of starting and ending Text from each Document
with open(filename) as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup1 in line or lookup2 in line:
            A.append(num)

# Appending each line in file to D list
            
with open(filename,'r') as f:
    for line in f:
        D.append(line)
# Extracting Meaningful text from each document and appending it to Para         
itr=len(A)            
Para=[]
i=0
while i<itr:
    Para.append(D[A[i]+1:A[i+1]-1])
    i=i+2    
    if i>itr-1:
     break
# Extracting Meaningful words from Para by using regular expression 
W=[]
for i in range(len(Para)):
    for line in Para[i]:
        for j in range(len(Para[i])):
            #print (i,j)
            W=W+(re.findall(r'[A-Za-z]+',Para[i][j]))         

# Filling unique words in Sample_Space of Words
counts = Counter(W)
Sample_Space=list(counts.keys())  
Sample_Space.sort()

'''
with open('Sample_Space.txt', 'w') as f:
    for item in Sample_Space:
        f.write("%s\n" % item)
Sample_Space=[]     

with open('Sample_Space.txt', 'r') as f:
    for line in f:
        Sample_Space.append(line)
                
        
'''
# Creating Document Term Matrix



M=np.empty([len(Para),len(Sample_Space)])
M=M.astype(int)
str=[]
Final=[]
for i in range(len(Para)):  
 str=" ".join(Para[i])
 Final.append(str)    

for i in range(len(Para)):
    for j in range(len(Sample_Space)):
         M[i][j]=Final[i].count(Sample_Space[j])
         

    
    
         
          

   

      
  

        

