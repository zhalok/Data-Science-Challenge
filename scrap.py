import requests
from bs4 import BeautifulSoup

# Replace with the URL of the webpage you want to scrape
url = "https://www.imdb.com/chart/top"

try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if there was an HTTP error

    # Create a BeautifulSoup object with the response content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find and extract the text from desired HTML elements
    # Example: Extract text from all <p> elements
    movies = soup.find("tr")
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))


except requests.RequestException as e:
    print(f"Error occurred while accessing the webpage: {e}")
except Exception as ex:
    print(f"An error occurred: {ex}")
