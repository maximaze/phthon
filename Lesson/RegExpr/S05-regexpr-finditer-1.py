# 정규표현식(Regular Expression)

import re

# findall()
# 정규식과 매치되는 모든 문자열을 찾아서 반복 가능한 객체로 리턴

# 영문자(대소문자)로 시작하는 문자열
p = re.compile("[a-zA-z]+")

content = "Life is too short, from 70 to 90 years."

result = p.finditer(content)

print('type: ', type(result))

for s in result: # Match object
    print(s, type(s))
    print('group: ', s.group()) # 매치된 문자열
    print(' span: ', s.span())  # 매치된 문자열의 시작, 끝에 해당하는 튜플
    print('start: ', s.start()) # 매치된 문자열의 시작 위치
    print('  end: ', s.end())   # 매치된 문자열의 끝 위치
    
    








