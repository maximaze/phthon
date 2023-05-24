# 정규표현식(Regular Expression)
# 문자클래스:
# \w : 문자 + 숫자
# \d : 숫자
# \s : whitespace(space, \t, \n)   

import re

content = "My info 'sunsinlee 010-1234-5678'"
print(content)

# 이름과 전화번호 형태의 문자열을 찾는 정규식
# 패턴 : 문자 공백 숫자 - 숫자 - 숫자
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+") # 문자 클래스
m = p.search(content)
print(m)

m = p.search("저를 소개합니다. 이순신 010-0707-0007")
print(m)