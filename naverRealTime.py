import urllib.request
import os
import sys
import pandas as pd
import time
from pandas import Series, DataFrame
from bs4 import BeautifulSoup

#네이버 api이용 아이디(수정해줘야함)
client_id ="userID"
client_secret ="secret"

#네이버 실시간 검색어 1위부터 20위까지
url_main = "http://naver.com"
response = urllib.request.urlopen(url_main)
soup = BeautifulSoup(response, "html.parser")
result1 = soup.select("span.ah_k")
for result in result1[:20]:
    encText = urllib.parse.quote(result.string)
    url_real = "https://search.naver.com/search.naver?where=realtime&sm=tab_jum&query="+ encText
    request = urllib.request.Request(url_real)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    print(result.string)
    if(rescode==200):
        response_body = response.read()
        soup = BeautifulSoup(response_body,"html.parser")
        news_craw = soup.select(
            'a'
        )
        for link in news_craw:
            print(link.get('href'))
        #print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
