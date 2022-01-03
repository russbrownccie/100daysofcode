from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_list = []
all_titles = soup.find_all(name="h3", class_="title")
for title in all_titles:
    movie_list.append(title.getText())
movie_list.reverse()
# print(movie_list)

with open("movies.txt", mode="w") as file:
    for movie in movie_list:
        file.write(movie + "\n")
