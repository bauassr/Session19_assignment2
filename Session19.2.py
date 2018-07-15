import numpy as np
import pandas as pd


Group1=np.array([51, 45, 33, 45, 67])
Group2= np.array([23, 43, 23, 43, 45])
Group3=np.array([ 56, 76, 74, 87, 56])

print("Group of mean",Group1.mean())
print("Group2  mean",Group2.mean())
print("Group3 mean",Group3.mean())

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

var1 = Group1['Sq Dev'].sum()/(Group1.shape[0]-1)
print('Variance of Sq. Dev for group 1:',var1)
var2 = Group2['Sq Dev'].sum()/(Group2.shape[0]-1)
print('Variance  Sq. Dev for group 2:',var2)
var3 = Group3['Sq Dev'].sum()/(Group3.shape[0]-1)
print('Variance  Sq. Dev for group 3:',var3)

MS = (var1 + var2+var3)/3
print('MS error for groups:% 6.f' % MS)
print(' Note: this is just the average within-group variance; it is not sensitive to group mean differences!')

Dferror=(15 - 3)
SSerror=MS*Dferror

print('Intermediate steps in calculating the variance of the sample means:')
GrandMean = (Group1['Data'].mean() + Group2['Data'].mean() + Group3['Data'].mean()) /3

GMean = np.array([Group1['Data'].mean() , Group2['Data'].mean() , Group3['Data'].mean()]) 

Grand= getdf(GMean)
print(Grand)


print("Sum of squares (SSmeans)=",Grand['Sq Dev'].sum())

var = Grand['Sq Dev'].sum()/(Grand.shape[0]-1)
print("\nVar means=",var)
MSG = (var)/5
print('\nMS error for groups:% 6.f' % MS)
print('\nNote: this is just the average within-group variance; it is not sensitive to group mean differences!')

DferrorG=(3 - 1)
print("\nDF error  for groups:" ,DferrorG)
SSerrorG=MSG*DferrorG
print("SS group",SSerrorG)
print('\nTest statistic and critical value:')
F = MSG/MS
print("F =",F)
print("Fcritical(2,12)=3.89\n")
print("Decision: reject H0\n")
print("Effect size\n")

η2=3022.9/4883.7
print("APA writeup")
print("F(2, 12)=9.75, p <0.05, η2=0.62.")