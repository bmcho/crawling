import requests as req
import re
'''
문자열 조작
find는 크롤링의 한계가 있다.
find를 통해서 크롤링을 한다기 보다는
크롤링을 하려고하는 주체가 존재여부를 확인 판단할때 사용하는 경우가 많다
True : 해당 index
False : -1
'''
res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")

html = res.text
pos = html.find("미국 USD")
s = html.split('<span class="value">')[1].split('</span')[0]
print(s)


'''
정규식
.*? : 범위 모두를 찾되 가장 적은 범위를 가져와라
'''
# r = re.compile(r"미국 USD.*?value\">(.*?)</", re.DOTALL)
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(html)
# print(captures)

for e in captures:
    print(f'{e[0]} : {e[1]}')

'''
쿼리 스트링
'''
res = req.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=감자")
print(res.text)
