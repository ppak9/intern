# 4,5 xlsx로 묶은 이후 마지막 실습으로 변경 
# 마지막 실습으로 변경
import requests
from bs4 import BeautifulSoup
import openpyxl

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

test =[]

# User-agent
url = 'https://datalab.naver.com/keyword/realtimeList.naver'
raw = requests.get(url,headers=headers)
# soup = BeautifulSoup(raw.content,'html.parser')
# result = soup.select('span.item_title_wrap')

# for item in result:
#     keyword = item.select_one('span.item_title').text.strip()
#     test.append(keyword)
test = input('입력해')
for n in range(1,100,10):
    raw = requests.get('https://www.google.com/search?biw=1536&bih=722&tbs=cdr%3A1%2Ccd_min%3A3%2F3%2F2020%2Ccd_max%3A9%2F4%2F2020&ei=sPBRX7TIBqbYhwOFkovwDw&q='+test)
    # url을 통해 기사 수집
    soup = BeautifulSoup(raw.text,'html.parser')
    # print(soup)
    # articles = soup.select("div.search")
    # print(articles)

    # for ar in articles:
    #     title = ar.select_one("h3.LC20lb DKV0Md").text
    #     print(title)
    #     # company = ar.select_one('span._sp_each_source').text
    #     # print(title,company)
    #     # sheet.append([title,company])

