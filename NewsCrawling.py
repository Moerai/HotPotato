import urllib.request
import os
import sys
import pandas as pd
import time
from pandas import Series, DataFrame
from bs4 import BeautifulSoup
#네이버 api이용 아이디
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

#네이버 실시간 검색어 1위부터 20위까지

url_main = "http://naver.com"
response = urllib.request.urlopen(url_main)
soup = BeautifulSoup(response, "html.parser")
result1 = soup.select("span.ah_k")

# for result in result1[:20]:
#    print(result.string)

#네이버 실시간 검색어의 뉴스데이터 가져오기
for result in result1[:20]:
    encText = urllib.parse.quote(result.string)
    url_news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+ encText
    url_news=url_news+encText
    request = urllib.request.Request(url_news)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    print(result.string)
    if(rescode==200):
        response_body = response.read()
        soup = BeautifulSoup(response_body,"html.parser")
        news_craw = soup.select(
            'dt > a'
        )
        for link in news_craw:
            try:
                url_news = link.get('href')
                #따옴표나 큰따옴표가 있으면 없애준다.
                def dequote(url_news):
                    if(url_news[0]==url_news[-1]) and url_news.startswith(("'",'"')):
                       return url_news[1:-1]
                    return url_news
                request = urllib.request.Request(url_news)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                soup = BeautifulSoup(response,"html.parser")
                response = soup.select("p")
                if(rescode==200):
                    #p태그 안에 있는 내용을 보여준다.
                    for result in response:
                        if not result.string == None:
                            if len(result.string)>=50:
                                print(result.string)
                else:
                    print("Error Code:" + rescode)
            except urllib.request.HTTPError as inst:
                output = format(inst)
                print(output)
    else:
        print("Error Code:" + rescode)
