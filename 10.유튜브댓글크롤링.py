from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv

#크롭 브라우져 생성
browser = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://www.youtube.com/watch?v=OFwcliQtcz8' #원하는 주소를 넣어준다. 

#웹사이트 열기
browser.get(url)
browser.implicitly_wait(10) #로딩이 끝날 때까지 10초를 기다려준다.

#스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

#무한 스크롤
#while before_h < 2: #스크롤 5번 내린다.
while True: #무한 스크롤

    browser.find_element_by_css_selector("body").send_keys(Keys.END) #모든 웹사이트는 body가 있다. 맨 아래 스크롤로 내린다. 
    time.sleep(1)

    #스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
#    before_h += 1

    if after_h == before_h:
        break
    before_h = after_h


f = open(r"C:\Python\웹크롤링\유튜브댓글크롤링.csv", 'w', encoding='UTF-8-sig', newline='')
csvWriter = csv.writer(f)

lists = browser.find_elements_by_css_selector("ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer")
Table = pd.DataFrame({"ID":[], "Comments":[], "Likes":[]}) #pd.DataFrame 만들 때 항목 추가 필요

for list in lists:
    id = list.find_element_by_css_selector('#author-text > span').text
    comments = list.find_element_by_css_selector('#content-text').text
    likes = list.find_element_by_css_selector('#vote-count-middle').text
    raw = pd.DataFrame({"ID":[id], "Comments":[comments], "Likes":[likes]}) #원하는 항목 추가 가능
    Table = Table.append(raw)
    csvWriter.writerow([id,comments,likes]) #한 행을 추가하겠다. 
print(Table)

