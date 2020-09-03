# 전주차 복습 영상, 네이버 영화 페이지 크롤링

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
url= 'https://movie.naver.com/movie/running/current.nhn'
raw = requests.get(url,headers=headers)

soup = BeautifulSoup(raw.text,'html.parser')

movie = soup.select('dl.lst_dsc')
for m in movie:
    title = m.select_one('dt.tit a').text
    star = m.select_one('div.star_t1 span.num').text
    genre = m.select_one('dl.info_txt1 dd span.link_txt a').text.strip()
    print(genre)

# 하나만 뽑는 방식
# score1 = soup.select('div.star_t1 a span.num')
# # 계층적으로 접근하는 방법
# print(score1[0].text)