# 핵심요소는 결국 페이지를 통해 넘어갈 수 있음을 얘기한다.

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

driver.get("https://v4.map.naver.com")

driver.find_elements_by_css_selector("button.btn_close")[1].click()

search_box = driver.find_element_by_css_selector('input#search-input')
search_box.send_keys('피자')

search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

for n in range(1,20):
    time.sleep(1)

    stores = driver.find_elements_by_css_selector("div.lsnx dl.lsnx_det")
    for store in stores:
        name = store.find_element_by_css_selector("dt a").text
        addr = store.find_element_by_css_selector("dd.addr").text
        try:
            phone = store.find_element_by_css_selector("dd.tel").text
        # 핵심요소 1: 예외처리를 통해 전화번호가 없을 경우 처리하는 방식
        except:
            phone = "없음"

        print(name, addr,phone)

    # 핵심요소 2 : page_nation을 위해 전체 select을 다 하는 방식을 추구 
    page_bar = driver.find_elements_by_css_selector("div.paginate > *")
    try:
        if n%5 ==0:
            page_bar[n%5+1].click()
        else:
            page_bar[6].click()
    # 핵심요소 3: 조건문에 따라 다음 수로 넘어가야 하니, 5로 나누었을 때 안 될 경우 계속해서 넘어가야 한다.
    except:
        print('수집완료!')
        break
    # 핵심요소 예외처리
        # lint 오류인지는 모르겠지만 phone이 먹지 않음

driver.close()