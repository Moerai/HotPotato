#모듈을 추출합니다.
import urllib.request
from bs4 import BeautifulSoup
import time
#기사목록을 가져옵니다.
url = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
#가져오는 방법은 select_one과 select가 있었다.
#select는 결과가 여러개가 나오고 아래와 같이 출력해준다.
#for result in results:
#   print(results.string)
#.string과 .attrs 두가지 타입으로 가져올 수 있었다.

#soup.select_one()
results =soup.select("#section_body a")
for result in results:
    #기사를 가져옵니다.
    print("제목 : ", result.attrs["title"])
    url_article = result.attrs["href"]
    response = urllib.request.urlopen(url_article)
    soup = BeautifulSoup(response, "html.parser")
    content = soup.select("#articleBodyContents")
    #가공합니다.
    output=""
    for item in content.contents:
        stripped =str(item).strip()
        if strippped =="":#비어있는 문자열은 출력ㄴㄴ
            continue
        if stripped[0] not in ["<","/"]:#<와 /는 출력ㄴㄴ
            output += str(item).strip()
    #필요없는 문자열을 빈문자열로 바꾼다.
    print(output.replace("본문 내용TV플레이어",""))

    #1초 휴식
    time.sleep(1)

#<실습2> 네이버 뉴스기사 목록 가져오기
