# 정규표현식(Regular Expression)

import re

# search()
# 문자열의 전체를 검색해서 정규식과 매치되는지 조사

str = "012345hello world"

p = re.compile('[a-z]+') # 반드시 알파벳으로 시작

# return : Match 객체
s = p.search(str)
print(s)
print(type(s))
if s:
    print('group: ', s.group()) # 매치된 문자열
    print(' span: ', s.span())  # 매치된 문자열의 시작, 끝에 해당하는 튜플
    print('start: ', s.start()) # 매치된 문자열의 시작 위치
    print('  end: ', s.end())   # 매치된 문자열의 끝 위치
    
    



