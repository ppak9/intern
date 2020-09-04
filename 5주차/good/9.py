from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
#############################################
# 추가
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#############################################

# urlretrieve("https://imgnews.pstatic.net/image/015/2020/09/03/0004410118_001_20200903180406260.jpg?type=w647",
#             "홍정욱.png")

# 확장

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=249'
raw = requests.get(url,headers=headers)
soup = BeautifulSoup(raw.text,'html.parser')

articles = soup.select('div.list_body li')
# print(articles)
for ar in articles:
    title = ar.select_one('dt a')
    # print(title)
    url2 = title.attrs['href']
    # print(url2)

    each = requests.get(url2, headers=headers)
    soup_each = BeautifulSoup(each.text,'html.parser')
    # print(soup_each)
    n = 1
    for target in soup_each:
        time = soup_each.select_one('span.t11').text
        # print(type(time))
        poster = soup_each.select_one('span.end_photo_org img')
        # print(poster)
        poster_src = poster.attrs['src']
        # print(poster_src)
        urlretrieve(poster_src, 'poster/'+ str(n) +'.jpg')

  