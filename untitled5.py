# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:02:57 2018

@author: john3
"""

from selenium import webdriver

browser=webdriver.Firefox(executable_path=r"C:\Users\john3\Downloads\geckodriver-v0.23.0-win64\geckodriver.exe")
browser.get("http://www.twitter.com")