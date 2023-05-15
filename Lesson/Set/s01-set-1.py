# 집합자료형(set)
# 셋은 집합 연산을 위한 자료형: 합집합, 교집합, 여집합, ...
# 셋은 키만 있는 딕셔너리 형태
# 중복을 허용하지 않음
#   - True, 1은 같은 값으로 취급하여 하나만 선택
#   - Flase, 0은 같은 값으로 취급하여 하나만 선택
# 순서가 없다(Unordered)

# 비어 있는 셋(set) 선언
# <class 'set'>
s = set()
print(type(s), ':', s)

s1 = set({1,3,5})
print(type(s1), ':', s1)

# set object이므로 dict.keys()가 없다.
# AttributeError: 'set' object has no attribute 'keys'
# s2 = set({10,8,6}.keys())
s2 = set({10,8,6})
print(type(s2), ':', s2)

##################################
# dict(keys) -> set
s3 = set({})
print(type(s3), ':', s3)

# dict(keys) -> set
s4 = set({}.keys())
print(type(s4), ':', s4)

# dict(values) -> set
s5 = set({}.values())
print(type(s5), ':', s5)

# dict(items) -> set
s6 = set({}.items())
print(type(s6), ':', s6)










