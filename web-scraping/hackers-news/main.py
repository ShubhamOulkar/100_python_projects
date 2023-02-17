import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://news.ycombinator.com/news")
news = response.text
soup = BeautifulSoup(news, 'html.parser')

# # save html file
# with open("news-web.html",mode='w') as file:
#     file.write(soup)

headings = soup.find_all("span",class_="titleline")

link = []
head = []

for i in range(len(headings)):
  head.append(headings[i].a.text)
  link.append(headings[i].a.get('href'))

score = soup.find_all("span", class_="score")

scores = []
for i in range(len(score)):
  scores.append(int(score[i].text.replace(" points","")))

dictionary = {"News Headings": head,
              "News Source Links":link,
              "Upvote":scores,
              }

news_table = pd.DataFrame(dictionary)

# TOP 5 upvoted news
print(news_table)
