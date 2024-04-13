import requests
import os

def open_termux(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            os.system('termux-open-url {}'.format(url))
            print("open browser")
        else:
            print("Error: Status code", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Contoh penggunaan:
if __name__ == "__main__":
    url = "https://www.youtube.com"  # Ganti dengan URL yang ingin Anda buka
    open_termux(url)
