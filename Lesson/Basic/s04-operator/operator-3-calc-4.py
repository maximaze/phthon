# 연산자 우선순위
# 괄호는 연산우선위가 가장 높다.
# 그러므로 가장 먼저 계산한다.

a = 10
b = 5
c = 2

d = a - b + c * 3
print('d=', d) # 11

# 괄호가 중첩되어 있으면 안쪽 괄호부터 바깥 괄호로 계산해서 나간다.
d = (a - (b + c)) * 3
print('d=', d) # d=9



