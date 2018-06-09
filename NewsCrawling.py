import urllib.request
import os
import sys
import pandas as pd
import time
from pandas import Series, DataFrame
from bs4 import BeautifulSoup
import datetime

request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

url_main = "http://naver.com"
response = urllib.request.urlopen(url_main)
soup = BeautifulSoup(response, "html.parser")
result1 = soup.select("span.ah_k")

# for result in result1[:20]:
#    print(result.string)


# for result in result1[:20]:
#     encText = urllib.parse.quote(result.string)
#     url_news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+ encText
#     url_news=url_news+encText
#     request = urllib.request.Request(url_news)
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request)
#     rescode = response.getcode()
#     print(result.string)
#     if(rescode==200):
#         response_body = response.read()
#         soup = BeautifulSoup(response_body,"html.parser")
#         news_craw = soup.select(
#             'dt > a'
#         )
#         for link in news_craw:
#             print(link.get('href'))
#         #print(response_body.decode('utf-8'))
#     else:
#         print("Error Code:" + rescode)
#크롤링시 불필요한 데이터 삭제 리스트
delReg = "[\\\\{}<>/!@#$%^&*='_■]"
naverDelList = ['서울연합뉴스', '사진연합뉴스', '이데일리', '플레이어', '뉴스1코리아', '서울경제', '오류를 우회하기 위한 함수 추가', '본문 내용', '무단 전재 및 재배포 금지', '사진', 'ⓒ', '세계를 보는 창', '경제를 보는 눈', '아시아경제', '무단전재',
                '배포금지.', '뉴스가 재밌다', '세상의 모든 재미', '티잼', '네이버 뉴스', '뉴스 스탠드에서도 만나세요', '뉴시스 페이스북 트위터', '공감언론', '뉴시스통신사', '( 연합뉴스)','아시아타임즈'
                '02)3701-5555', '구독신청:', '대한민국 오후를 여는 유일석간', '문화일보', '모바일 웹', '문화닷컴 바로가기', '▶', '()',  '【', '】', '.."', '[', ']', '©', '  ','데일리안','스페셜경제','기자','일간투데이','MBC 캡처'
               ,'국제뉴스','(청도)']

#호출하는 날짜와 시간
dt = datetime.datetime.now()
dt.strftime("%Y%m%d%H%M%S")

#네이버 실시간 검색어의 뉴스데이터 가져오기(인덱스를 조절하여 범위 조절가능) anaconda3\\news\\아래 저장
#Todo
dt = datetime.datetime.now()
folTime = dt.strftime("%Y%m%d%H%M%S")
os.mkdir("C:\\Users\\frien\\Anaconda3\\news\\"+folTime)
#네이버 실시간 검색어의 뉴스데이터 가져오기
for result in result1[0:20]:
    encText = urllib.parse.quote(result.string)
    url_news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+ encText
    url_news=url_news+encText
    request = urllib.request.Request(url_news)

    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    print(result.string)
    key = result.string
    news_save_fuc = "C:\\Users\\frien\\Anaconda3\\news\\"+folTime+"\\"+key+".txt"
    print(news_save_fuc)
    news_save=open(news_save_fuc,'w',encoding='utf-8')
    news_text = result.string + "\n"
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
                sleep(0.1)
                response = urllib.request.urlopen(request)
                sleep(0.1)
                rescode = response.getcode()
                sleep(0.1)
                soup = BeautifulSoup(response,"html.parser")
                response = soup.select("p")
                #p태그 안에 있는 내용을 보여준다.
                for result in response:
                    if not result.string == None:
                        if len(result.string)>50:
                            news_all = result.string
                            for i in naverDelList:
                                for char in delReg:
                                    news_all = news_all.replace(char,"")
                                    news_all = news_all.replace(i,"")
                            print(news_all)
                            news_text = (news_text + news_all)
            except (urllib.request.HTTPError, http.client.IncompleteRead, ConnectionError) as inst:
                output = format(inst)
                print(output)
        news_save.write(news_text)
        news_save.close()
    else:
        print("Error Code:" + rescode)
        news_save.close()
        
