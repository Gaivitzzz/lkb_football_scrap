import requests
from bs4 import BeautifulSoup

url = "https://www.ballthai.com/ช้างเอฟเอคัพ/"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser") 

    
    all_html = str(soup)  

    
    print(all_html)

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")