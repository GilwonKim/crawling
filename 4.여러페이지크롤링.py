import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요")
lastpage = pyautogui.prompt("마지막 페이지를 입력하세요(숫자만)")
pagenum = 1
#네이버 서버에 대화를 시도
for i in range(1,int(lastpage)*10,10):
    print(f"{pagenum}페이지 입니다++++++++++++++++++++++++++++++++++")
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}"
    response = requests.get(url)
    #네이버에서 html을 줌
    html = response.text

    #html 번역 선생님으로 수프를 만ㄴ듦
    soup = BeautifulSoup(html,'html.parser')

    #id 값이 NM_set_home_btn인 놈 한 개를 찾아 냄
    #클래스는 '.' 그리고 아이디는 '#'
    word = soup.select(".news_tit") #결과는 리스트

    for link in word:
        title = link.text #태그 안에 텍스트 요소를 가져온다. 
        url = link.attrs['href'] #href의 속성값을 가져온다. 
        print(title,url)

    #텍스트 요소만 출력
    pagenum += 1
