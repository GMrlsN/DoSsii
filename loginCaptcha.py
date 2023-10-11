import requests
from bs4 import BeautifulSoup
import threading
from twocaptcha import TwoCaptcha
solver = TwoCaptcha('YOUR_API_KEY')

# Define the URL of the login page
login_url = "https://sii.itq.edu.mx/sistema/index.php"
control_number = 20140936
nip = 8194

result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                          url='https://mysite.com/page/with/recaptcha')

session = requests.Session()

    # Prepare the data for the POST request
data = {
        "no_de_control": control_number,
        "password": nip,
    }

    # Send a POST request to the login page
response = session.post(login_url)
print(response.text)