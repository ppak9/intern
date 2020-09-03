# 링크를 타고 가 해당 영상 정보를 가지고 올 수 있음이 핵심
# bs 로는 youtube 크롤링 못함! js 다 삭제해야 하는데, 이는 parsing 기능만 제공하는 bs의 경우 불가능

# 유튜브 대도서관 크롤링
# 대도서관 영상 수 좋아요 합은?

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
url ='https://www.youtube.com/BuzzBean/videos'
raw = requests.get(url,headers=headers)

soup = BeautifulSoup(raw.content,'html.parser')
# print(soup)
title = soup.find_all('a')
print(title)
# info = soup.select('ytd-grid-playlist-renderer.style-scope ytd-grid-renderer')
# print(info)