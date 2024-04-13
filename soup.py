import requests
from bs4 import BeautifulSoup

url = 'https://facebook.com/login'

# Fetch the HTML content of the URL using requests
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Now you can work with the parsed HTML content (soup) as needed
    print(soup.prettify())  # This will print the prettified HTML content
else:
    print('Failed to retrieve the website:', response.status_code)
