# final 결과본

import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.parse import quote_plus
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

url = 'https://search.shopping.naver.com/best100v2/main.nhn'

raw = requests.get(url,headers=headers)

soup = bs(raw.text,'html.parser')

target = soup.select('p.cont > a')

##### middle 1 #####
for i in target:
    url2 = i.attrs['href']
    html = urlopen(url2)
    soup2 = bs(html,'html.parser')
    img = soup2.find_all('img')

    n=1
    for i in img:
        imgUrl = i.attrs['src']
        if 'https://ssl.pstatic.net' in imgUrl:
            continue
        fullname = 'poster/'+ str(n) +'.jpg'
        urlretrieve(imgUrl,fullname)

        n+=1
print('완료!')


