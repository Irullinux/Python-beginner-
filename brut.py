import requests
from bs4 import BeautifulSoup
urltarget= "http://192.168.0.1"
    
    payload = {
    'userName' : root,
    'pcPassword' : root
    }
with: requests.session() as s:
    s.post(urltarget, data=payload)
# Contoh penggunaan:
if __name__ == "__main__"
