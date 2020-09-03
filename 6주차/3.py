# 연습 과제 바꾸기

from selenium import webdriver
import time


target = input('검색할 내용을 쓰시오')

driver = webdriver.Chrome('./chromedriver')
driver.get('https://papago.naver.com/')

time.sleep(1)

search_name = driver.find_element_by_css_selector('textarea#txtSource')
search_name.send_keys(target)

search_button = driver.find_element_by_css_selector('button#btnTranslate')
search_button.click()

time.sleep(0.5)
result = driver.find_element_by_css_selector('div#targetEditArea').text
print(result)

time.sleep(2)

driver.close()
