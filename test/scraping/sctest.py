#지금까지 공부한 것 정리
import urllib.request
from bs4 import BeautifulSoup

url = "http://finance.naver.com/marketindex/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
#가져오는 방법은 select_one과 select가 있었다.
#select는 결과가 여러개가 나오고 아래와 같이 출력해준다.
#for result in results:
#   print(results.string)
#.string과 .attrs 두가지 타입으로 가져올 수 있었다.

#soup.select_one()
results =soup.select("span.value")

print("달러 환율: ", results[0].string) #달러 환율
print("엔 환율: ", results[0].string) #엔화 환율
print("유로 환율: ", results[0].string) #유로 환율

#<실습1> 미국환율가져오기
