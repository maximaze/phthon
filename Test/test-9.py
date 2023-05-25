'''
[문제9] 주민등록번호와 전화번호를 검색하는
        정규표현식을 파이썬으로 코딩하라.
'''
import re

data = "박상철 910816-1234567 010-8843-5467"

p1 = re.compile('[0-9]+[-]+[0-9]+')
p2 = re.compile('[0-9]+[-]+[0-9]+[-]+[0-9]+')

m1 = p1.search(data)
m2 = p2.search(data)

if m1:
    print('주민등록번호:',m1.group())

if m2:
    print('전화번호:',m2.group())



