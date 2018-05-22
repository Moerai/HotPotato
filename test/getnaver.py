import urllib.request
import urllib.parse

# 방식 : GET
# 대상 : https://search.naver.com=>호스트 이름
# 추가적인 정보
# -경로: /search.naver
# -데이터
# ?where=nexearch
# &sm=top_hty
# &fbm=1
# &ie=utf8
# &query=초콜릿
#%EC%B4%88%EC%BD%9C%EB%A6%BF

api = "https://search.naver.com/search.naver"
values = {
    "where":"nexearch",
    "sm":"top_hty",
    "fbm":"1",
    "ie":"utf8",
    "query":"초콜릿"
}
params =urllib.parse.urlencode(values)
url = api+"?"+params

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
