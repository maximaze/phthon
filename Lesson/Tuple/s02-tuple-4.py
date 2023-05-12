# 튜플은 값을 변경할 수 없다.

# 튜플 생성
t1 = (1, '하나', 'two', 3.14)
print(t1)

# 값을 대입하여 변경할 수 없다. 
# TypeError: 'tuple' object does not support item assignment
# t1[0] = 2
# print(t1[0])

# 요소를 삭제할 수 없다.
# TypeError: 'tuple' object doesn't support item deletion
# del t1[0]

# 인덱스가 범위를 넘어서면 오류
# IndexError: tuple index out of range
# print(t1[4])
# print(t1[-5])




