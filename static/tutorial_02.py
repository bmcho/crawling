import requests as req
from bs4 import BeautifulSoup as BS 

url = "https://naver.com"
res = req.get(url)
soup = BS(res.text, "html.parser")

print(soup.title)