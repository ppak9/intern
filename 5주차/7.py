# 실습 과제: IMDB 영화 정보 크로링 통해 csv로 저장하기

import requests
from bs4 import BeautifulSoup

f = open('test.csv','w',encoding='utf-8')
f.write('title,rate \n')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

url ='https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'
raw = requests.get(url,headers=headers)

soup =BeautifulSoup(raw.text,'html.parser')

# 중간 print로 확인해보는 작업 얘기해주기
# print(soup)
container = soup.select('tbody > tr')
for info in container:
    title = info.select_one('td.titleColumn > a').text.strip()
    rate = info.select_one('td.ratingColumn').text.strip()
    f.write(title + ',' + rate + '\n')

f.close()