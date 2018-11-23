# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:57:58 2018

@author: john3
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#np.corrcoef(x,y)

df=pd.DataFrame({"a":np.random.randint(0,50,1000)})
df["b"]=df["a"]+np.random.normal(0,10,1000)#positively correlated with "a"
df["c"]=100-df["a"]+np.random.normal(0,5,1000)#negatively correlated with "a"
df["d"]=np.random.randint(0,50,1000) #not correlated with "a"

pd.scatter_matrix(df, figsize=(6,6) )
plt.show()
print(df.corr())



