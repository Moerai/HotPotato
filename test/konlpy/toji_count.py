import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
#utf-16 인코딩으로 파일을 열고 글자를 출력하기
fp = codecs.open("BEXX0003.txt","r",encoding="utf-16")

#파일에서 데이터를 가져와서 text에 담기
soup = BeautifulSoup(fp,"html.parser")
body = soup.select_one("body > text")
text = body.getText()

#텍스트를 한 줄씩 처리하기
twitter=Twitter()
word_dic={}
lines = text.split("\n")
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if not(word[0] in word_dic):
            word_dic[word[0]]=0
        word_dic[word[0]]+=1

#많이 사용된 명사 출력하기
keys= sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}{1}".format(word, count),end="")
print()
