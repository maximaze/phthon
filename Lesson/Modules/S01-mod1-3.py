# S01-mod1-3.py
#
# import:
#   - 현재 디렉터리에 있는 파일(모듈)
#   - 파이썬의 라이브러리가 저장된 디렉터리에 있는 모듈

# 사용할 필요한 함수만 선택적으로 임포트

# from 모듈이름 import 모듈함수 [, 모듈함수, ...]
# from mod1 import add,sub

# from 모듈이름 import *
from mod1 import *

# 모듈이름 생략
a = add(10,20)
b = sub(10,3)

print('a=',a)
print('b=',b)
print('a+b=',a+b)
print('a=',a,'b=',b)



