## 라이브러리에 대한 수업 필수

import requests
from bs4 import BeautifulSoup

test = requests.get('https://tv.kakao.com/r')
# print(test.text)

html = BeautifulSoup(test.text,"html.parser")
print(html)

# BeautifulSoup에 대한 의의를 말해 주어야 함
# html 기준으로 parsing 이 가능
# 파싱은 지난 번 얘기한 문자열에서 설명한 파싱이라고 언급