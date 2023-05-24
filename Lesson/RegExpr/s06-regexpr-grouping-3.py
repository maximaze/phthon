# 정규표현식(Regular Expression)

import re

# 그룹핑(Grouping)
# 문자열을 반복해서 조사하는 정규식

# 그룹핑 : 괄호로 감싼다.
# "ABC"가 한 번 이상 반복
p = re.compile("(ABC)+")
m = p.finditer("ABCABCABC OK! ABCX")

print(m)

for s in m:
    print(s.group(), type(s.group()))   # 0번째 문자열
    print(s, type(s))
    print('group: ', s.group()) # 매치된 문자열
    print(' span: ', s.span())  # 매치된 문자열의 시작, 끝에 해당하는 튜플
    print('start: ', s.start()) # 매치된 문자열의 시작 위치
    print('  end: ', s.end())   # 매치된 문자열의 끝 위치
