from bs4 import BeautifulSoup

html = """
<html>
<body>
    <div id="meigen">
        <h1>위키북스 도서</h1>
        <ul class = "items">
            <li>유니티 게임 이펙트 입문</li>
            <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
            <li>모던 웹사이트 디자인의 정석</li>
        </ul>
    </div>
</body>
</html>
"""
#CSS선택자 5가지
#테그선택자
# "ul"
# "li"
# "div"
#아이디선택자
# "#<id이름>"
#테그.class이름이 제일 많이 쓰인다.
#"ul.book.art.it.items"이렇게 이어서 사용이 가능하다.
#후손 선택자
#후손은 아래의 모든 것, 자식은 바로 아래에 있는 것 둘은 다름
#"#meigen li"
#자식 선택자
#"ul.items > li"

#html가져오기
soup = BeautifulSoup(html, 'html.parser')

#요소
header = soup.select_one("body > div > h1")

#요소의 배열
list_items = soup.select("ul.items > li")

#글자를 추출하는 경우
print(header.string)

#속성을 가지고 있는 경우에 사용
print(soup.select_one('ul').attrs)

for li in list_items:
    print(li.string)
