# 정규표현식(Regular Expression)

import re

# search()
# 문자열의 전체를 검색해서 정규식과 매치되는지 조사

str = "12345 hello world"

p = re.compile('[a-z]+') # 반드시 알파벳으로 시작

# return : Match 객체
s = p.search(str)
print(s)


if s != None:
    print('s.span: ', s.span(), type(s.span()))
    sp, ep = s.span()
    print(str[sp:ep])



