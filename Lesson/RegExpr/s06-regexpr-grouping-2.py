# 정규표현식(Regular Expression)

import re

# 그룹핑(Grouping)
# 문자열을 반복해서 조사하는 정규식

# 그룹핑 : 괄호로 감싼다.
# "ABC"가 한 번 이상 반복
p = re.compile("(ABC)+")
m = p.search("ABCABCABC OK! ABCX")

print(m)
print(m.group(), type(m.group()))   # 0번째 문자열
print(m.group(0), type(m.group(0))) # 0번째 문자열
print(m.group(1), type(m.group(1))) # 1번째 문자열