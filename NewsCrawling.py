import urllib.request
import os
import sys
import pandas as pd
import time
from pandas import Series, DataFrame
from bs4 import BeautifulSoup
#���̹� api�̿� ���̵�
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

#���̹� �ǽð� �˻��� 1������ 20������

url_main = "http://naver.com"
response = urllib.request.urlopen(url_main)
soup = BeautifulSoup(response, "html.parser")
result1 = soup.select("span.ah_k")

# for result in result1[:20]:
#    print(result.string)

#���̹� �ǽð� �˻����� ���������� ��������
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
                #����ǥ�� ū����ǥ�� ������ �����ش�.
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
                    #p�±� �ȿ� �ִ� ������ �����ش�.
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
