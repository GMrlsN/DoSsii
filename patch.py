import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from stem import Signal
from stem.control import Controller
from pypasser import reCaptchaV2

control_number = 20140936
nip = 8194

# Function to change Tor IP
def change_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_tor_password")  # Replace with your Tor password
        controller.signal(Signal.NEWNYM)

# Create an instance of webdriver with Tor proxy
proxy_settings = {
    "proxyType": "manual",
    "httpProxy": "127.0.0.1:8118",  # This is the default Tor proxy address
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.popups": 0})
chrome_options.add_experimental_option("prefs", {"download.default_directory": "/tmp"})
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050")  # This is the default Tor SOCKS proxy address
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

time.sleep(20)
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
    login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-default" and @type="submit"]')
    login_button.click()
    
    while True:
        print("attack...")
        driver.get("https://sii.itq.edu.mx/sistema/modulos/cons/alumnos/horario.php")
        # Change Tor IP periodically (e.g., every 10 minutes)
        time.sleep(600)  # Sleep for 10 minutes
        change_tor_ip()
else:
    print('FAIL')
