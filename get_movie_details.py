import requests
from bs4 import BeautifulSoup
import os
from scrap_list import scrap_list
import pandas as pd


def get_movie(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        summary = soup.find(
            "span", {"class": "sc-2eb29e65-1 goRLhJ"}).get_text().strip()

        poster = soup.find("img", {"class": "ipc-image"}).get("src")
        title = soup.find(
            "h1", {"data-testid": "hero__pageTitle"})
        title = title.get_text().strip()
        cast_section = soup.find(
            "div", {"class": "sc-52d569c6-3 jBXsRT"})
        casts = cast_section.find_all(
            "div", {"class": "ipc-metadata-list-item__content-container"})
        director = casts[0].get_text().strip()
        writers = casts[1].find_all("li")
        writers = [writer.get_text().strip() for writer in writers]

        stars = casts[2].find_all("li")
        stars = [star.get_text().strip() for star in stars]
        genre = soup.find("div", {"data-testid": "genres"}).get_text().strip()
        data = {}
        data["summary"] = summary
        data["title"] = title
        data["director"] = director
        data["writers"] = writers
        data["stars"] = stars
        data["poster"] = poster
        data["genre"] = genre

        return data

    except requests.RequestException as e:
        print(f"Error occurred while accessing the webpage: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")


def get_movies():
    movie_links = scrap_list()

    movie_data = []
    for movie_link in movie_links:
        data = get_movie("https://www.imdb.com" + movie_link)
        movie_data.append(data)
        print("Data scrapped", len(movie_data))
    # print(movie_data)
    dataframe = pd.DataFrame(movie_data)
    dataframe.to_json(os.path.join(
        "datasets", "movies.json"), orient='records')
    # dataframe.to_csv("movies.csv", index=False)


get_movies()
