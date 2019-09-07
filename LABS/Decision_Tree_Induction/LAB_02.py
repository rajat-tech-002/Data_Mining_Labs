# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 00:17:36 2019

@author: Rajat_PC
"""
result=[]
import random as rand
import pandas as pd
file='test.csv'
#file='train_data.csv'
data=pd.read_csv(file)
for i in range(data.shape[1]-1):
    result.append(pd.crosstab(index=data.iloc[:,i],columns=data.iloc[:,4]))
#print(result)    
    #print("\n")
    ## Doing Laplacian Correction 
     # Increase size of freuencies by 1
     
for i in range(len(result)):
     lencol=len(result[i].columns)
     lenrow=len(result[i].index)
     for j in range(lenrow):
         for k in range(lencol):
             result[i].iloc[j][k]=result[i].iloc[j][k]+1
             
# Probability Calc             
for i in range(len(result)):
    lencol=len(result[i].columns)
    lenrow=len(result[i].index)
    result[i]['Total']=0
    result[i].loc['Total']=0
    for j in range(lenrow):
     result[i].iloc[j]['Total']=sum(result[i].iloc[j])
    for k in range(lencol+1):
     result[i].loc['Total'][k]=sum(result[i][result[i].columns[k]])
     
# Convert int64 to flaot in all values     
for i in range(len(result)):
  result[i]=result[i].astype(float)     
     
for i in range(len(result)):
     lencol=len(result[i].columns)
     lenrow=len(result[i].index)
     for j in range(lenrow):
         for k in range(lencol):
             if k==lencol-1:
               result[i].iloc[j][k]=(result[i].iloc[j][k])/(result[i].loc['Total']['Total'])  
             else:
               result[i].iloc[j][k]=(result[i].iloc[j][k])/(result[i].iloc[j][lencol-1])
    
## Conditional probabilities

 # Taking random sample
classes=len(list(result[0].columns))-1
features=len(data.columns)-1
Classes=list(result[0].columns)

Feat=[]
#for i in range(feat-1):
 #   var.append('Feat'+str(i))
    
for i in range(features):   
    temp=len(result[i].index)-1
    Feat.append(list(result[i].index[0:temp]))

Rsample=[]    
for i in range(features):    
 Rsample.append(rand.sample(Feat[i],1))

P=[]
# Finding conditional probability per class

for i in range(classes):
    P.append(result[0].loc[Rsample[0]][Classes[i]][0]*result[1].loc[Rsample[1]][Classes[i]][0]*result[2].loc[Rsample[2]][Classes[i]][0]*result[3].loc[Rsample[3]][Classes[i]][0]*result[0].loc['Total'][Classes[i]])
#print(P)    
    s=sum(P)
for i in range(len(P)):
    P[i]=P[i]/s
print('\n')    
print('Random sample formed is:\n')       
print(Rsample)
print('\n')
id=P.index(max(P))
print('Most Probable Class is\n',Classes[id], '\nWith', P[id]*100 ,'%')
    


    

 
              
        
     


             
     
     

    
    