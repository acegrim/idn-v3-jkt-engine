import requests
import time

def is_internet_available():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def main():
    max_retries = 88888
    retry_interval = 30  # Wait for 30 seconds before retrying
    
    retries = 0

    while not is_internet_available():
        print("No internet connection. Waiting for connection...")
        time.sleep(retry_interval)
        retries += 1
        
        if retries >= max_retries:
            print("Maximum retries reached. Exiting the script.")
            break

    if is_internet_available():
        print("Internet connection available. Continuing script execution...")
        
        python_scripts = [
            "Adel.py",
            "Alya.py",
            "Amanda.py",
            "Anindya.py",
            "Ashel.py",
            "Callie.py",
            "Cathy.py",
            "Chelsea.py",
            "Chika.py",
            "Christy.py",
            "Cynthia.py",
            "Daisy.py",
            "Danella.py",
            "Eli.py",
            "Elin.py",
            "Ella.py",
            "Feni.py",
            "Fiony.py",
            "Flora.py",
            "Freya.py",
            "Gendis.py",
            "Gita.py",
            "Gracia.py",
            "Gracie.py",
            "Greesel.py",
            "Indah.py",
            "Indira.py",
            "Jeane.py",
            "Jessi.py",
            "Kathrina.py",
            "Lia.py",
            "Lulu.py",
            "Lyn.py",
            "Marsha.py",
            "Michie.py",
            "Muthe.py",
            "Olla.py",
            "Oniel.py",
            "Raisha.py",
            "Shani.py",
            "Zee.py",
            "JKT48-Official.py"
        ]

        for script in python_scripts:
            print(f"Executing script: {script}")
            exec(open(script).read())  # Execute the script directly
            
            time.sleep(1)  # Wait for 1 second before running the next script

if __name__ == '__main__':
    main()
