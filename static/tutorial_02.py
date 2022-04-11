from re import L
from unicodedata import name
import requests as req
from bs4 import BeautifulSoup as BS 

url = "https://naver.com"
res = req.get(url)
soup = BS(res.text, "html.parser")

print(soup.title)
print(soup.title.string)


url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

# print(tds)

for td in tds:
  if len(td.find_all("a")) == 0:
    continue

  print(td.get_text(strip=True))

  print(td.string)

  print(td.strings)
  for s in td.strings:
    print(s)

  print(td.stripped_strings)
  for s in td.stripped_strings:
    print(s)


names = []
for td in tds:
  if len(td.find_all("a")) == 0:
    continue
    
  names.append(td.get_text(strip=True))

prices = []
for td in tds:
  if "class" in td.attrs:
    if "sale" in td.attrs['class']:
      prices.append(td.get_text(strip=True))


print(names)
print(prices)

names = []
for td in soup.select("td.tit"):
  names.append(td.get_text(strip=True))

prices= []
for td in soup.select("td.sale"):
  prices.append(td.get_text(strip=True))

print(names)
print(prices)

  