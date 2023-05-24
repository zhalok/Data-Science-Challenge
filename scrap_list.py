import requests
from bs4 import BeautifulSoup
import json

# Replace with the URL of the webpage you want to scrape


def process_link_address(links):
    len_ = len(links)
    for i in range(len_):
        id = links[i].split("/")[2]
        links[i] = "https://www.imdb.com/title/" + id
    return links


def remove_duplicates_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


def scrap_list(url):

    # url = "https://www.imdb.com/chart/top"
    # url = "https://www.imdb.com/search/title/?genres=action&start=51&explore=title_type,genres&ref_=adv_nxt"

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if there was an HTTP error

        # Create a BeautifulSoup object with the response content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find and extract the text from desired HTML elements
        # Example: Extract text from all <p> elements
        # movies = soup.find_all("td", {"class": "titleColumn"})
        movies = soup.find_all("a")
        # print(movies)

        links = [movie.get("href") for movie in movies if type(
            movie.get("href")) == str and movie.get("href").startswith("/title")]

        # links = [link.get("href") for link in links if type(
        #     link.get("href")) == str and link.get("href").startswith("/title")]
        links = process_link_address(links)
        links = remove_duplicates_preserve_order(links)

        return links

    except requests.RequestException as e:
        print(f"Error occurred while accessing the webpage: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")


# movies = scrap_list()


# for i in range(len(movies)):
#     print(movies[i])
