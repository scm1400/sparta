
# bs4: 브라우저가 보고있는 것 중에서 내가 원하는 것을 솎아내는 작업을 해줌
import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%B0%95%EB%B3%B4%EC%98%81")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')


thumbnails = soup.select('#imgList > div > a > img')

i=1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img,f'imgs_homework/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫주기