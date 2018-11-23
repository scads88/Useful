# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:02:19 2018

@author: john3
"""
import os
dirName="ministock"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:    
    print("Directory " , dirName ,  " already exists")