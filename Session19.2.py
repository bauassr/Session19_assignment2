import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy as s
import matplotlib.pyplot as plt
import math


Group1=np.array([51, 45, 33, 45, 67])
Group2= np.array([23, 43, 23, 43, 45])
Group3=np.array([ 56, 76, 74, 87, 56])


Group1=np.array([51, 45, 33, 45, 67])
Group2= np.array([23, 43, 23, 43, 45])
Group3=np.array([ 56, 76, 74, 87, 56])

print(Group1.mean())
print(Group2.mean())
print(Group3.mean())

def getdf(value):
    Group = pd.DataFrame(value, columns={"Data"})
    Group['Mean']= Group['Data'].mean() 
    st =  Group['Data'] - Group['Mean']
    Group['Deviation']=st
    Group['Sq Dev']=st*st
    return Group
    

Group1 = getdf(Group1)
print(Group1.head())
Group2 = getdf(Group2)
print(Group2.head())
Group3 = getdf(Group3)
print(Group3.head())
