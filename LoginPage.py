# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:02:08 2020

@author: dell-pc
"""

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#usr = input("Enter Email")
#pwd = input("Enter password")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://upxacademy.learnyst.com/login')
print("UPX Opened")
sleep(1)

username = driver.find_element_by_id('lernystLogin_new_user_user_email')
username.send_keys('')
print("")
password = driver.find_element_by_id('lernystLogin_new_user_user_password')
password = driver.fin
password.send_keys('Madhavi@1996')
print("Password Entered")
LoginButton = driver.find_element_by_id('lr_login_btn')
if LoginButton.click():
    print('Logged In Succesfully')
else :
    print("Failed")
    

