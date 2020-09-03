# 같이 실습: 네이버 영화 가지고오기

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
url= 'https://movie.naver.com/movie/running/current.nhn'
raw = requests.get(url,headers=headers)

soup = BeautifulSoup(raw.text,'html.parser')

# movie = soup.select('dl.lst_dsc')
# for m in movie:
#     title = m.select_one('dt.tit a').text
#     star = m.select_one('div.star_t1 span.num').text
# float형에 대한 언급(지난번 파이선 강의 때 언급해 드린 부분)
    
rate = soup.select('dl.info_exp div.star_t1 span.num').text
for r in rate:
    if float(r)< 10.0:
        print('*')
    else:
        print(r)
# 오류 scenario
# 예상 오류 지점, select 와 select_one의 구별이 안 될 경우
#     "ResultSet object has no attribute '%s'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?" % key
# bs 에 find_all 이라는 것을 찾아야 함

# 좀 더 재밌게 예매율로 변환하기