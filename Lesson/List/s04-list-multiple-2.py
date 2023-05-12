# 리스트 곱하기(*)
# 리스트 곱하기는 리스트를 주어진 숫자만큼 
# 반복해서 항목을 더해서 붙인다.

a = [1,3,5]
b = a + a
print('a=', a, type(a))
print('b=', b, type(b))

# 리스트의 각 요소를 참조
a0 = a[0]
a1 = a[1]
a2 = a[2] 
print('a0=', type(a0))
print('a1=', type(a1))
print('a2=', type(a2))

# 개별적으로 연산을 수행하면
# 각 요소들을 꺼내서 그 자료형(type)에 맞는 연산을 수행
x = a[0] + a[1] + a[2] # list -> number(int)
print('list->number(int): x=', x, type(x))

# a는 리스트가 아니라 class int
# TypeError: 'int' object is not subscriptable
# a0 = x[0]
# a1 = x[1]
# a2 = x[2] 
# print(type(a0), type(a1), type(a2))


# 3 * int(9) -> 27
c = 3 * x
print('3 * b = ', c)

print('[9]: ', [9], 'type([9]):', type([9]))