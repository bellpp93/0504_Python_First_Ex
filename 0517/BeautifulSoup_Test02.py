"""
    네이버 서울날씨 웹 크롤링 예제
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 네이버 검색창에서 서울날씨 검색한 URL 주소
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
temperature = soup.find(class_='temperature_text')
weather = soup.find(class_='weather before_slash')

print(temperature.text)
print(weather.text)