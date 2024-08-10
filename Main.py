from bs4 import BeautifulSoup
import requests
url="https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(url)
content=response.text
movies_List=[]
soup=BeautifulSoup(content,"html.parser")
movies_All=soup.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")
for movie in movies_All:
    movies_List.append(movie.getText())

movies_List.reverse()

with open("moviesList.txt","w") as file:
    file.write(str.join("\n",movies_List))