import pandas as pd
file='test.csv'
data=pd.read_csv(file)
for i in range(data.shape[1]-1):
    result=pd.crosstab(data.iloc[:,i],data.iloc[:,4])
    print(result)
    print("\n")
