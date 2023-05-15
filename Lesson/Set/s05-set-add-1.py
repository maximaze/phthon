# 셋에 데이터를 추가
# add

# 값을 1개 추가
s1 = set([1,2,3])
print(s1)
s1.add(5)
print(s1)

# 산술연산자(+)는 지원하지 않음
# TypeError: unsupported operand type(s)
# s2 = s1 + set([4,6])
# print(s2)

# 합집합을 이용하면 더하기(+) 효과와 같다.
s2 = s1 | set([4,6])
print(s2)
