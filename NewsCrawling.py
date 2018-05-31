import urllib.request
import os
import sys
import pandas as pd
import time
from pandas import Series, DataFrame
from bs4 import BeautifulSoup

# 네이버 실시간 검색어 1위부터 20위까지

url_main = "http://naver.com"
response_main = urllib.request.urlopen(url_main)
soup = BeautifulSoup(response_main, "html.parser")
result1 = soup.select("span.ah_k")

# for result in result1[:20]:
#    print(result.string)

# 네이버 실시간 검색어의 뉴스데이터 가져오기
url_news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + encText
for result in result1[:20]:
    encText = urllib.parse.quote(result.string)
    url_news = url_news + encText
    request = urllib.request.Request(url_news)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))