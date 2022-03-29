import requests
from bs4 import BeautifulSoup

#네이버 서버에 대화를 시도
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"
response = requests.get(url)

#네이버에서 html을 줌
html = response.text

#html 번역 선생님으로 수프를 만듦
soup = BeautifulSoup(html,'html.parser')

#id 값이 NM_set_home_btn인 놈 한 개를 찾아 냄
#클래스는 '.' 그리고 아이디는 '#'
word = soup.select(".news_tit") #결과는 리스트
for link in word:
    title = link.text #태그 안에 텍스트 요소를 가져온다. 
    url = link.attrs['href'] #href의 속성값을 가져온다. 
    #텍스트 요소만 출력
    print(title,url)
