import requests
from bs4 import BeautifulSoup

url='https://tv.kakao.com/category/drama'
raw = requests.get(url)
# 여기서 한 번 끊기, requests의 역할이 무엇인지를 확인하기 위해

html = BeautifulSoup(raw.text,'html.parser')

clips=html.select("a.link_contents")

# 지난번 반복한 list 에 관련한 rule들을 그대로 가지고 오면 됨

for k in clips:
    title = k.select_one("strong.tit_item")
    channel = k.select_one("span.txt_item")
    print(title.text.strip())
    print(channel.text.strip())