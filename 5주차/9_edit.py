from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus


#############################################
# 추가
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#############################################

# urlretrieve("https://imgnews.pstatic.net/image/015/2020/09/03/0004410118_001_20200903180406260.jpg?type=w647",
#             "홍정욱.png")

# 확장

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
test = input('name?')
url = base_url +quote_plus(test)
# raw = requests.get(url,headers=headers)
html = urlopen(url)
# print(type(html))
# raw = requests.get(url,headers=headers)
# soup = BeautifulSoup(html,'html.parser')
soup = BeautifulSoup(html,'html.parser')


    # each = requests.get(url2, headers=headers)
    # soup_each = BeautifulSoup(each.text,'html.parser')
img = soup.find_all(class_='_img')
# print(img)

n=1
for i in img:
    imgUrl = i['data-source']
    # poster_src = i.attrs['data-source']
    # 마지막 urlretrieve 저장
    # print(imgUrl)
    fullname = 'poster/'+ str(n) +'.jpg'
    urlretrieve(imgUrl,fullname)
#   print(poster_src)
    n+=1
print('완료!')
  