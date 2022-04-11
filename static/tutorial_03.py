from bs4 import BeautifulSoup as BS
import requests as req

url = "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0+%EC%BC%80%EC%9D%B4%EC%8A%A4&bt=-1&frm=NVSCPRO"

res = req.get(url)
soup = BS(res.text, "html.parser")

arr = soup.select("ul.list_basis div>a:first-child[title]")

for a in arr:
  print(a.get_text(strip=True))

print("")

url ="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"

res = req.get(url, headers={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
})

soup = BS(res.text, "html.parser")
arr = [x.get_text(strip=True) for x in soup.select("div.name")]

for a in arr:
  print(a)

print("")

for desc in soup.select("div.descriptions-inner"):
  ads = desc.select("span.ad-badge")
  if len(ads) == 0:
    print(desc.select("div.name")[0].get_text(strip=True))