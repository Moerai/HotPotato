import requests
#실패 다음처럼 복잡한 싸이트에서는 안되는듯ㅠㅠ...
#세션 만들기
session = requests.session()
#로그인
url= "https://logins.daum.net/accounts/srp.do?slevel=1&rid=0b21501b-94f3-42bb-991b-bc8c25e8e894&srplm1=352a293e65e632ece975898f66ef059a7e105433d16d0a53c047a16c105a89ad"
data = {
    "url":"www.daum.net",
    "slevel":"1",
    "luid":"055f2712-b883-421f-a629-fe12928b11da:1526403707617:Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F66.0.3359.170+Safari%2F537.36:211.177.172.199:toploginform",
    "id":"skyinss",
    "pw":""
}

response = session.post(url, data=data)
response.raise_for_status()

#다음을 시작페이지로 들고오기
url = "https://www.daum.net/"
response = session.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")
soup.select_one(#homepage)

#서버에 대한 이해보다 스크레이핑에 요청방식이 중요하다.
#session.post(url)
#session.put(url)
#session.delete(url)
