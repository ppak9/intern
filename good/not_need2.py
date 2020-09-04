#1,2,3 .py 다 같이 하나 강의로 

import requests
from bs4 import BeautifulSoup

f = open('kakaotv.csv','w',encoding='utf8')
#[scenario 1] utf-8 언급 -> 구글링
f.write('제목,채널')
#[scenario 2] write는 내부 안에서

# 순서 바꾸어보아도 상관 없음!

url='https://tv.kakao.com/category/drama'
raw = requests.get(url)
# 여기서 한 번 끊기, requests의 역할이 무엇인지를 확인하기 위해


html = BeautifulSoup(raw.text,'html.parser')

clips=html.select("a.link_contents")

for k in clips:
    title = k.select_one("strong.tit_item").text.strip()
    channel = k.select_one("span.txt_item").text.strip()
    # [scenario 3] text 형태로의 변환이 없을 경우 <class 'bs4.element.Tag'>로 들어오게 됨
    f.write(title +','+channel +'\n')

f.close()