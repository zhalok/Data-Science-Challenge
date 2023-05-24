import requests
from bs4 import BeautifulSoup

# Replace with the URL of the webpage you want to scrape


def scrap_list():

    url = "https://www.imdb.com/chart/top"
    # url = "https://www.imdb.com/search/title/?genres=action&start=51&explore=title_type,genres&ref_=adv_nxt"

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if there was an HTTP error

        # Create a BeautifulSoup object with the response content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find and extract the text from desired HTML elements
        # Example: Extract text from all <p> elements
        movies = soup.find_all("td", {"class": "titleColumn"})
        # for i in movies:
        #     print(i.get_text())
        links = [movie.find("a") for movie in movies]

        links = [link.get("href") for link in links if type(
            link.get("href")) == str and link.get("href").startswith("/title")]

        return links

    except requests.RequestException as e:
        print(f"Error occurred while accessing the webpage: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")


movies = scrap_list()
for i in movies:
    print(i)
