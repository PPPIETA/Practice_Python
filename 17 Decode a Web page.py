import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
page = requests.get(url)
text = page.text

soup = BeautifulSoup(text,"lxml")
for title in soup.find_all(class_="story-heading"):
    if title.a:
        print(title.a.text.replace("\n"," ").strip())
    else:
        print(title.contents[0].replace("\n"," ").strip())
