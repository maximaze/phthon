# 정규표현식(Regular Expression)

import re

# findall()
# 정규식과 매치되는 모든 문자열을 리스트로 리턴

# 영문자(대소문자)로 시작하는 문자열
p = re.compile("[a-zA-z]+")

content = "Life is too short, from 70 to 90 years."

result = p.findall(content)

print('type: ', type(result))
print(result)




