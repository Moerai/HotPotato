def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res
def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r
a = "오늘 강남에서 맛있는 스파게티를 먹었다."
b = "강남에서 먹었던 오늘의 스파게티는 맛있었다."
# 2-gram
r2, word2 = diff_ngram(a, b, 2)
print("2-gram:", r2, word2)
# 3-gram
r3, word3  = diff_ngram(a, b, 3)
print("3-gram:", r3, word3)

c = "본문과 전혀 관계 없는 내용이지만 마시멜로는 맛있습니다."
d = "마시멜로는 본문과 전혀 관계 없이 맛있습니다."
# 2-gram
r2, word2 = diff_ngram(c, d, 2)
print("2-gram:", r2, word2)
# 3-gram
r3, word3  = diff_ngram(c, d, 3)
print("3-gram:", r3, word3)

e = "파이썬 프로그래밍에서 중요한 것은 불록입니다."
f = "겨울에는 충분한 수분을 보충해야 합니다."
# 2-gram
r2, word2 = diff_ngram(e, f, 2)
print("2-gram:", r2, word2)
# 3-gram
r3, word3  = diff_ngram(e, f, 3)
print("3-gram:", r3, word3)
