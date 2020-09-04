# 중간 과제 네이버 기사 가지고오기

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=249'
raw = requests.get(url,headers=headers)
soup = BeautifulSoup(raw.text,'html.parser')

articles = soup.select('div.list_body li')
# print(articles)
for ar in articles:
    title = ar.select_one('dt a')
    url2 = title.attrs['href']
    # print(url)

    each = requests.get(url2, headers=headers)
    soup_each = BeautifulSoup(each.text,'html.parser')
    # print(soup_each)

    result = soup_each.select('div.article_info > h3')
    # print(result)
    for r in result:
        print(r.text)