# 중간과제 네이버 실시간 검색어 가져오기

import requests
from bs4 import BeautifulSoup

f = open('navernews.csv','w',encoding='utf8')
#[scenario 1] utf-8 언급 -> 구글링
f.write('제목,채널')
#[scenario 2] write는 내부 안에서

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

# User-agent
url = 'https://datalab.naver.com/keyword/realtimeList.naver'

raw = requests.get(url,headers=headers)
soup = BeautifulSoup(raw.text,'html.parser')

target = soup.select('div.item_box')

for result in target:
    title = result.select_one('span.item_title').text
    rank = result.select_one('span.item_num').text
    print(title,rank)
    f.write(title +','+rank +'\n')

f.close()
