import requests
from bs4 import BeautifulSoup

url = "https://www.ballthai.com/ผลบอลสด/"  # Replace with the URL you want to scrape

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    soup = BeautifulSoup(response.content, "html.parser")  # Parse the HTML

    # Get all HTML content
    all_html = str(soup)  # Convert the entire BeautifulSoup object to a string

    # Find all MP4 links (more specific approach)
    print(all_html)

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")