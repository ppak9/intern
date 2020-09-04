# import requests
# requests 랑 urllib의 차이를 언급하기
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
test = input('name?')
url = base_url + test
# raw = requests.get(url,headers=headers)
html = urlopen(url)
# print(type(html))
soup = BeautifulSoup(html,'html.parser')
img = soup.find_all(class_='_img',limit=10)

n=1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img/'+ test + str(n)+'.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n +=1
print('다운로드 완료')

