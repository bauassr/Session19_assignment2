import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy as s
import matplotlib.pyplot as plt
import math


Group1=np.array([51, 45, 33, 45, 67])
Group2= np.array([23, 43, 23, 43, 45])
Group3=np.array([ 56, 76, 74, 87, 56])

print(Group1.mean())
print(Group2.mean())
print(Group3.mean())

Group1 = pd.DataFrame(Group1, column={"Data"})