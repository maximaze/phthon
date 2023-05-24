# 정규표현식(Regular Expression)

import re

# match()
# 문자열의 처음부터 정규식과 매치되는지 조사

p = re.compile('[a-z]+') # 반드시 알파벳으로 시작

print(p.match('python'))
print(p.match('python is easy!'))

# 매지되지 않으면 None을 리턴
print(p.match('3.0 python is easy!'))

s = "hello world"
m = p.match(s)
if m != None:
    print('m.span: ', m.span(), type(m.span()))
    sp, ep = m.span()
    print(s[sp:ep])




