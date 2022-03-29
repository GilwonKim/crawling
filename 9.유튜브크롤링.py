from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv

#크롭 브라우져 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

#웹사이트 열기
browser.get('https://www.youtube.com')
browser.implicitly_wait(10) #로딩이 끝날 때까지 10초를 기다려준다.

browser.find_element_by_name('search_query').click()
time.sleep(1.5)  
browser.find_element_by_name('search_query').send_keys("진단검사실")
time.sleep(1.5)
browser.find_element_by_name('search_query').send_keys(Keys.ENTER)
time.sleep(1.5)

#스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

#무한 스크롤
while before_h < 2: #스크롤 5번 내린다.
#while True:

    browser.find_element_by_css_selector("body").send_keys(Keys.END) #모든 웹사이트는 body가 있다. 맨 아래 스크롤로 내린다. 
    time.sleep(1)

    #스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    before_h += 1

#    print(after_h)
#    if after_h == before_h:
#        break
#    before_h = after_h

#lists = browser.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer')


f = open(r"C:\Python\웹크롤링\유튜브검색결과크롤링.csv", 'w', encoding='UTF-8-sig', newline='')
csvWriter = csv.writer(f)


lists = browser.find_elements_by_css_selector("#contents > ytd-video-renderer")
Table = pd.DataFrame({"Title":[], "Links":[], "Views":[], "Date":[]}) #pd.DataFrame 만들 때 항목 추가 필요

for list in lists:
#    name = list.find_element_by_css_selector('#text > a').text
#    duration = list.find_element_by_css_selector('#overlays > ytd-thumbnail-overlay-time-status-renderer > span').text
#    regdate_ment = list.find_element_by_css_selector('#metadata-line > span:nth-child(2)').text
    title = list.find_element_by_css_selector('h3.title-and-badge.style-scope.ytd-video-renderer > a').text
    link = list.find_element_by_css_selector('h3.title-and-badge.style-scope.ytd-video-renderer > a').get_attribute("href")
    view = list.find_element_by_css_selector('#metadata-line > span:nth-child(1)').text
    date = list.find_element_by_css_selector('#metadata-line > span:nth-child(2)').text

    raw = pd.DataFrame({"Title":[title], "Links":[link], "Views":[view], "Date":[date]}) #원하는 항목 추가 가능

    Table = Table.append(raw)
    csvWriter.writerow([title,link,view,date]) #한 행을 추가하겠다. 
print(Table)