import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

url = 'https://v4.map.naver.com/'

raw = requests.get(url,headers=headers)
soup = BeautifulSoup(raw.text,'html.parser')

target = soup.select('div.lsnx')

# 페이지에 저장되어 있는 정적페이지를 그대로 가지고 온다면 
# 인형 뽑기마냥 계속해서 결과물이 변화하는 것이라고 비유표현을 들음