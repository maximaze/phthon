# 함수, 글로벌 변수
# 변수의 범위
# 함수에서 선언되어 있느 ㄴ벼수는 하뭇 밖에서 접근할 수 없다.
# 전역변수 :
#   - 함수에서는 함수 밖에서 선언된 전역변수를 참조할 수 있다.
#   - 함수 안에서는 전역변수를 바꿀 수 없다.

# 전역변수 : 함수 밖에서 선언된 변수
x = 20

def func(a):
    # UnboundLocalError: local variable 'x' referenced before assignment
    # x를 지역변수로 인식하려고 해서 오류
    # 함수 안에서는 전역변수를 바꿀 수 없으므로 지역변수로 처리를 하려함
    # 그런데 x + 90에서 x가 지역변수에 없으므로 오류가 발생
    # x = x + 90
    a += x # x를 전역변수로 인식
    return a # 값을 리턴(call by value)

#%%
y = func(x)     # x의 값 20을 전달 : call by value

print('x=', x) # x: 전역변수, 20
print('y=', y) # y: 전역변수, 119
