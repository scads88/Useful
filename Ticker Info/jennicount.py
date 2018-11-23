# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 01:07:14 2018

@author: john3
"""

import pandas as pd
df=pd.read_csv(r"C:\Users\john3\OneDrive\Desktop\jenniwidget.csv") #imports doc
df["College"]=df["College"].str.upper() #capitalizes all in dfcol1
df["College"]=df["College"].str.replace("’",'')#weird apostrophe removed
df["College"]=df["College"].str.replace(" ", '')#space removed
df["College"]=df["College"].str.replace(".", "")#period removed
df["College"]=df["College"].str.replace("'", "")#normal apostrophe removed
df=df.sort_values(by=['College'], inplace=False, ascending=True)#alphabetically ordered
df.reset_index(drop=True, inplace=True)
df['count'] = df.groupby('College')['College'].transform('count')#generates a count
df=df.drop_duplicates("College")#gets rid of duplicate counts made from transformation
df.to_csv(r"C:\Users\john3\OneDrive\Desktop\jennicounts.csv") #output to new csv file name

print(df.head())
    