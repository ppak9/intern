from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

driver.get("https://v4.map.naver.com")

driver.find_elements_by_css_selector("button.btn_close")[1].click()

search_box = driver.find_element_by_css_selector('input#search-input')
search_box.send_keys('피자')

search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

for n in range(1,5):
    time.sleep(1)

    stores = driver.find_elements_by_css_selector("div.lsnx dl.lsnx_det")
    for store in stores:
        name = store.find_element_by_css_selector("dt a").text
        addr = store.find_element_by_css_selector("dd.addr").text
        # phone = store.find_element_by_css_selector("dd.tel").text
        
        print(name, addr)

    # 페이지를 넘어가면서 클릭하기 위해서는 
    page_bar = driver.find_elements_by_css_selector("div.paginate > *")
    page_bar[n+1].click()

        # lint 오류인지는 모르겠지만 phone이 먹지 않음

driver.close()