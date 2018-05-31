import urllib.request
from bs4 import BeautifulSoup
import time

url = "http://naver.com"

response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")

result1 = soup.select("span.ah_k")
# result2 = soup.select("span.ah_r") 랭킹순위
for result in result1[:20]:
    print(result.string)


# todo list
#for 구문을 이용해서 반복구문을 제거한다.
#네이버 검색어를 검색후 나오는 뉴스들의 제목 출력
#기사 내용도 출력 특수문자 없애고 출력
#실시간검색 내용보기
