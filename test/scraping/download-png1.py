#라이브러리 읽어 들이기
import urllib.request

#URL과 저장 경로 지정하기 http://uta.pw/shodou/img/28/214.png
url = "http://api.aoikujira.com/ip/ini"


#savename = "test.png"

#다운로드
mem = urllib.request.urlopen(url).read()
print(mem.decode("utf-8"))



#2
# with open(savename, mode="wb")as f:
#     f.write(mem)
#     print("저장되었습니다.")

#1
# urllib.request.urlretrieve(url, savename)
# print("저장되었습니다.")
