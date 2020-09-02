import requests
from bs4 import BeautifulSoup
import openpyxl

wb=openpyxl.Workbook()
sheet=wb.active

# sheet.append 를 사용할 경우 list로 업데이트 해 나감
sheet.append(['제목','채널'])

url='https://tv.kakao.com/category/drama'
raw = requests.get(url)
# 여기서 한 번 끊기, requests의 역할이 무엇인지를 확인하기 위해


html = BeautifulSoup(raw.text,'html.parser')

clips=html.select("a.link_contents")

# 지난번 반복한 list 에 관련한 rule들을 그대로 가지고 오면 됨

for k in clips:
    title = k.select_one("strong.tit_item").text.strip()
    channel = k.select_one("span.txt_item").text.strip()
    # [scenario 3] text 형태로의 변환이 없을 경우 <class 'bs4.element.Tag'>로 들어오게 됨
    sheet.append([title,channel])
    # csv 는 comma 로서 구분이 가능한 확장 파일이지만 xlsx 의 경우 저렇게 append 안에 list형태로 나아가야함

wb.save('test2.xlsx')