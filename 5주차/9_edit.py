from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.parse import quote_plus
# urlopen 과 requests 의 차이 언급
from bs4 import BeautifulSoup as bs

# 보안 ssl 얘기(간단히)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input('name?')
url = base_url +quote_plus(plus_url)

# soup 다른 라이브러리 설명
html = urlopen(url)
# html 그대로를 가지고 오는 방식
soup = bs(html,'html.parser')
img = soup.find_all(class_='_img')
# 다른 라이브러리 제시

######여기서 끊기#####

# 반복문 예시
# logic을 통해 변경
n=1
for i in img:
    imgUrl = i['data-source']
    fullname = 'poster/'+ plus_url + str(n) +'.jpg'
    urlretrieve(imgUrl,fullname)
    n+=1
print('완료!')
  