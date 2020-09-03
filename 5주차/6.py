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
    rate = m.select_one('dl.info_exp div.star_t1 span.num').text
    if float(rate)< 5.0:
        print('*')
    else:
        print(title)

# float형에 대한 언급(지난번 파이선 강의 때 언급해 드린 부분)

# 좀 더 재밌게 예매율로 변환하기