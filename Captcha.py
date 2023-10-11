import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import sys
import pydub
import speech_recognition as sr
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from datetime import datetime
import requests
import json
from webdriver_manager.chrome import ChromeDriverManager

# Recaptcha libraries
import speech_recognition as sr
import requests
import urllib
import pydub
control_number = 20140936
nip = 8194
def delay():
    time.sleep(random.randint(2, 3))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://sii.itq.edu.mx/sistema/")


time.sleep(2)


# 👇️ using find_element method 👇️
search_field = driver.find_element(By.ID, 'usr')
search_field.send_keys(control_number)
search_field = driver.find_element(By.ID, 'pwd')
search_field.send_keys(nip)

time.sleep(50)
#driver.switch_to.default_content()
#driver.switch_to.frame(recaptcha_div.find_element(By.TAG_NAME, 'iframe'))
#recaptcha_checkbox = driver.find_element(By.ID, 'recaptcha-anchor')
#recaptcha_checkbox.click()
while True:
    print("attack...")
    driver.get("https://sii.itq.edu.mx/sistema/modulos/cons/alumnos/horario.php")
    
time.sleep(200)

driver.close()


