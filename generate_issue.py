import codecs
import cgi
from bs4 import BeautifulSoup
import urllib.request
from konlpy.tag import Twitter
import os, re, json, random
dict_file = "hotissue-data.json"
dic = {}
twitter = Twitter()

# 문장 만들기
def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic"
    top = dic["@"]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == ".": break
        w1, w2 = w2, w3
    ret = "".join(ret)
    return ret
def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))
# 딕셔너리에 데이터 등록하기
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1
# 마르코프 체인 딕셔너리 만들기
def make_dic(words):
    tmp = ["@"]
    dic = {}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == ".":
            tmp = ["@"]
            continue
    return dic

fp = codecs.open("C:\\Users\\frien\\Anaconda3\\news\\#YYYYMMDDHHmmss\\재목.txt", "r", encoding="utf-8")
text = fp.read()
# 형태소 분석
twitter = Twitter()
malist = twitter.pos(text, norm=True)
words = []
for word in malist:
    # 구두점 등은 대상에서 제외(단 마침표는 포함)
    if not word[1] in ["Punctuation"]:
        words.append(word[0])
    if word[0] == ".":
        words.append(word[0])
    # 딕셔너리 생성
    dic = make_dic(words)
    json.dump(dic, open(dict_file,"w", encoding="utf-8"))
# 문장 만들기
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print("---")
