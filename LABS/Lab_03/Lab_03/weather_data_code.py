import numpy as np
import pandas as pd
eps = np.finfo(float).eps
from numpy import log2 as log
import pprint
from sklearn.metrics import accuracy_score

def find_entropy(df):
    Class = df.keys()[-1]  # To make the code generic, changing target variable class name
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value] / len(df[Class])
        entropy += -fraction * np.log2(fraction)
    return entropy


def find_entropy_attribute(df, attribute):
    Class = df.keys()[-1]  # To make the code generic, changing target variable class name
    target_variables = df[Class].unique()  # This gives all 'Yes' and 'No'
    variables = df[attribute].unique()  # This gives different features in that attribute (like 'Hot','Cold' in Temperature)
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute] == variable][df[Class] == target_variable])
            den = len(df[attribute][df[attribute] == variable])
            fraction = num / (den + eps)
            entropy += -fraction * log(fraction + eps)
        fraction2 = den/ len(df)
        entropy2 += -fraction2 * entropy
    return abs(entropy2)


def find_splitnode(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
        IG.append(find_entropy(df) - find_entropy_attribute(df, key))
    return df.keys()[:-1][np.argmax(IG)]


def get_subtable(df, node, value):
    return df[df[node] == value].reset_index(drop=True)


def buildTree(df, tree=None):
    Class = df.keys()[-1] 
    node = find_splitnode(df)
    attValue = np.unique(df[node])
    # Create an empty dictionary to create tree
    if tree is None:
        tree = {}
        tree[node] = {}
    # We make loop to construct a tree by calling this function recursively.
    # In this we check if the subset is pure and stops if it is pure.
    for value in attValue:
        subtable = get_subtable(df, node, value)
        clValue, counts = np.unique(subtable[df.keys()[-1]], return_counts=True)
        if len(counts) == 1:  # Checking purity of subset
            tree[node][value] = clValue[0]
        else:
            tree[node][value] = buildTree(subtable)  # Calling the function recursively
    return tree
def predict(inst,tree):
    for nodes in tree.keys():
        value=inst[nodes]
        tree=tree[nodes][value]
        prediction=0
        if(type(tree) is dict):
            prediction=predict(inst,tree)
        else:
            prediction=tree
            break
    return prediction
file='test.csv'
df=pd.read_csv(file)
tree=buildTree(df)
pprint.pprint(tree)
y_true=['yes','yes','yes','yes','no']
data=[{'outlook':'rainy','temperature':'mild','humidity':'normal','windy':False},
      {'outlook':'sunny','temperature':'mild','humidity':'normal','windy':True},
      {'outlook': 'overcast', 'temperature': 'mild', 'humidity': 'high', 'windy': True},
      {'outlook': 'overcast', 'temperature': 'hot', 'humidity': 'normal', 'windy': False},
      {'outlook': 'rainy', 'temperature': 'mild', 'humidity': 'high', 'windy': True},]
y_pred=[]
for dic in data:
    inst=pd.Series(dic)
    prediction=predict(inst,tree)
    y_pred.append(prediction)
print('Accuracy Score(%):',accuracy_score(y_true,y_pred)*100)