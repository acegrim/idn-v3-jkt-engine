import subprocess
import os
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
    retry_interval = 30  # Jeda 30 detik sebelum mencoba kembali
    
    retries = 0

    while not is_internet_available():
        print("Tidak ada koneksi internet. Menunggu koneksi kembali...")
        time.sleep(retry_interval)
        retries += 1
        
        if retries >= max_retries:
            print("Batas maksimum percobaan tercapai. Keluar dari skrip.")
            break

    if is_internet_available():
        print("Koneksi internet tersedia. Melanjutkan eksekusi skrip...")
        
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

        
        line_counter = 0
        
        for script in python_scripts:
            subprocess.Popen(["python", script], shell=True)
            time.sleep(1)  # Jeda 40 detik sebelum menjalankan file .py berikutnya
            
            line_counter += 1
            
            if line_counter % 30000 == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
            
            # Tunggu semua subprocess selesai sebelum melanjutkan ke file .py berikutnya
            time.sleep(1)

if __name__ == '__main__':
    main()
