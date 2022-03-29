from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

#크롭 브라우져 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

#웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) #로딩이 끝날 때까지 10초를 기다려준다.


#쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

search = browser.find_element_by_css_selector('input.co_srh_input._input') #검색창 선택 
search.click()

search.send_keys('목베게')
search.send_keys(Keys.ENTER)


#무한 스크롤 내리기======================

#현재 스크롤 위치
scroll = browser.execute_script('return window.scrollY')

while True:
    #맨 아래로 스크롤을 내린다
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    #스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    #마지막 스크롤 위치
    after_h = browser.execute_script('return window.scrollY')
    if after_h == scroll:
        break
    scroll = after_h

#파일 생성
#f = open(r"C:\Python\data.csv", 'w', encoding='UTF-8-sig', newline='')
#csvWriter = csv.writer(f)


#상품 정보 DIV
items = browser.find_elements_by_css_selector('basicList_info_area__17Xyo')

for item in items:
    name = item.find_element_by_css_selector('basicList_title__3P9Q7').text
    try:
        price = item.find_element_by_css_selector('price_num__2WUXn').text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector('basicList_title__3P9Q7 > a').get_attribute('href')
    print(name,price,link)

#    csvWriter.writerow([name,price,link]) #한 행을 추가하겠다. 

#파일 닫기
#f.close()