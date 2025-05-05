from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empires_webpage = response.text
soup = BeautifulSoup(empires_webpage, "html.parser")

rank_titles = soup.select("h3.title")
film_launch_year_raw = soup.select("strong")

movies_dict = {}

for item in rank_titles:
    text = item.get_text()
    if ")" in text:
        rank, title = text.split(")", 1)
        rank = int(rank.strip())
        title = title.strip()

        movies_dict[rank] = {"title": title}

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for rank in sorted(movies_dict):
        title = movies_dict[rank]["title"]
        file.write(f"{rank}. {title}\n")