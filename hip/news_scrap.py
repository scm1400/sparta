from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

# print(articles)

for article in articles:
    title = article.select_one('div.news_wrap.api_ani_send > div > a').text
    url = article.select_one('div.news_wrap.api_ani_send > div > a')['href']
    print(title, url)



driver.quit()