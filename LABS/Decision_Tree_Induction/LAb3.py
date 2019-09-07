# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:11:41 2019

@author: Rajat_PC
"""

# Decision Tree Classifier
result=[]
import math
import pandas as pd
###################################################
def H(p):
    if p==0:
        return 0
    return p*math.log(p,2)
###################################################
def func_info_gain(result):
 total=result[0]['Total']['Total']    
 prob_yes=result[0].loc['Total']['yes']/total
 prob_no=result[0].loc['Total']['no']/total
 E_play= -(H(prob_yes))- (H(prob_no))
 for i in range(len(result)):
    E=[]
    for j in range(len(result[i].index)-1):
     prob_yes=result[i].loc[result[i].index[j]]['yes']/result[i].loc[result[i].index[j]]['Total']
     prob_no=result[i].loc[result[i].index[j]]['no']/result[i].loc[result[i].index[j]]['Total']
     Entropy=-(H(prob_yes))-(H(prob_no))
     E.append(Entropy)
    I=0
    for k in range(len(E)):
        I=I+(result[i].loc[result[i].index[k]]['Total']/total)*E[k]
    Info.append(I)    
     
 Info_gain=E_play-Info 
 
 max_info_gain=max(Info_gain)
 for i in range(len(Info_gain)):
    if Info_gain[i]==max_info_gain:
      max_info_gain_feat=i
      break
 return E,Info,max_info_gain_feat
###################################################
##################################################
def func_create_result(data):
 result1=[]
 for i in range(data.shape[1]-1):
    result1.append(pd.crosstab(index=data.iloc[:,i],columns=data.iloc[:,data.shape[1]-1]))
 for i in range(len(result1)):
    lencol=len(result1[i].columns)
    lenrow=len(result1[i].index)
    result1[i]['Total']=0
    result1[i].loc['Total']=0
    for j in range(lenrow):
     result1[i].iloc[j]['Total']=sum(result1[i].iloc[j])
    for k in range(lencol+1):
     result1[i].loc['Total'][k]=sum(result1[i][result1[i].columns[k]])
 return result1
#################################################### 
file='test.csv'


#file='train_data.csv'
data=pd.read_csv(file)
    
result= func_create_result(data)     
len_f=len(data.columns)-1
Feat=data.columns[0:len_f] 


Info=[]
# Calculating Entropies of all features for selecting root node and 
# getting index of feature selected for root
E,I,max_info_gain_feat=func_info_gain(result)
#Select Root with max info gain

    
# Create tables for Outlook- Overcast, Rainy, Sunny
reduced_table=[]
temp=pd.DataFrame()
for i in range(len(result[max_info_gain_feat].index)-1):
    temp=data.loc[data[Feat[max_info_gain_feat]]==result[max_info_gain_feat].index[i]]
    temp=temp.set_index(Feat[max_info_gain_feat])
    reduced_table.append(temp)

new_result=[] 
for i in range(len(reduced_table)):
    new_result.append(func_create_result(reduced_table[i]))
    
###################################################
result=new_result[0]
total=result[0]['Total']['Total']    
prob_yes=result[0].loc['Total']['yes']/total
prob_no=0
E_play= -(H(prob_yes))- (H(prob_no))
## Since Entropy[play]=0 Tree root for overcast is play=yes
###################################################
# for rainy
Info=[]
Info_gain=[]
result=new_result[1] 
total=result[0]['Total']['Total']    
prob_yes=result[0].loc['Total']['yes']/total
prob_no=result[0].loc['Total']['no']/total
E_play= -(H(prob_yes))- (H(prob_no))
for i in range(len(result)):
    E=[]
    for j in range(len(result[i].index)-1):
     prob_yes=result[i].loc[result[i].index[j]]['yes']/result[i].loc[result[i].index[j]]['Total']
     prob_no=result[i].loc[result[i].index[j]]['no']/result[i].loc[result[i].index[j]]['Total']
     Entropy=-(H(prob_yes))-(H(prob_no))
     E.append(Entropy)
     
    I=0

    for k in range(len(E)):
        I=I+(result[i].loc[result[i].index[k]]['Total']/total)*E[k]
    Info.append(I)    
     
Info_gain=E_play-Info 
 
max_info_gain=max(Info_gain)
for i in range(len(Info_gain)):
    if Info_gain[i]==max_info_gain:
      max_info_gain_feat=i
      break   
## So rainy chooses windy here
# Windy becomes a child under rainy branch
# for sunny
Info=[]
Info_gain=[]
result=new_result[2] 
total=result[0]['Total']['Total']    
prob_yes=result[0].loc['Total']['yes']/total
prob_no=result[0].loc['Total']['no']/total
E_play= -(H(prob_yes))- (H(prob_no))
for i in range(len(result)):
    E=[]
    for j in range(len(result[i].index)-1):
     prob_yes=result[i].loc[result[i].index[j]]['yes']/result[i].loc[result[i].index[j]]['Total']
     prob_no=result[i].loc[result[i].index[j]]['no']/result[i].loc[result[i].index[j]]['Total']
     Entropy=-(H(prob_yes))-(H(prob_no))
     E.append(Entropy)
     
    I=0

    for k in range(len(E)):
        I=I+(result[i].loc[result[i].index[k]]['Total']/total)*E[k]
    Info.append(I)    
     
Info_gain=E_play-Info 
 
max_info_gain=max(Info_gain)
for i in range(len(Info_gain)):
    if Info_gain[i]==max_info_gain:
      max_info_gain_feat=i
      break  
      
## Continuing this the tree comes like this
## Making tree
from anytree import Node, RenderTree
feat1 = Node('outlook')
feat2 = Node('sunny',parent=feat1)
feat3 = Node('overcast',parent=feat1)
feat4 = Node('rainy',parent=feat1)
feat5 = Node('humidity',parent=feat2)
feat6 = Node('high',parent=feat5)
feat7 = Node('normal',parent=feat5)
feat8 = Node('no',parent=feat6)
feat9 = Node('yes',parent=feat7)
feat10 = Node('wind',parent=feat4)
feat11= Node('strong',parent=feat10)
feat12= Node('weak',parent=feat10)
feat13= Node('no',parent=feat11)
feat14= Node('yes',parent=feat12)



for pre, fill, node in RenderTree(feat1):
    print("%s%s" % (pre, node.name))

 
    
    
    






   