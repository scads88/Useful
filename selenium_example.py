# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:02:57 2018

@author: john3
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
browser=webdriver.Firefox(executable_path=r"C:\Users\john3\Downloads\geckodriver-v0.23.0-win64\geckodriver.exe")
browser.implicitly_wait(10)
browser.get("https://www.marketwatch.com/investing/stock/aapl/profile")

"""
browser_iframe = WebDriverWait(browser, 10).until(
    ec.presence_of_element_located(
        (
            By.TAG_NAME, 'iframe'
        )
    )
)
        """