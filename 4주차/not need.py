# 중간과제 네이버 실시간 검색어 가져오기

import requests
from bs4 import BeautifulSoup

# f= open('test.csv','w')
# f.write('제목')
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

# User-agent
url = 'https://datalab.naver.com/keyword/realtimeList.naver'
raw =requests.get(url,headers=headers)
soup = BeautifulSoup(raw.content,'html.parser')
result = soup.select('span.item_title_wrap')
for item in result:
    keyword=item.select_one('span.item_title').text.strip()
    print(keyword)

# for k in result:
#     title=k.select_one('span.keyword').text.strip()
#     # f.write(title+'\n')
#     print(type(title))
# # f.close()