# 함수, 글로벌 변수
# 변수의 범위
# 함수에서 선언되어 있느 ㄴ벼수는 하뭇 밖에서 접근할 수 없다.

# 전역변수 : 함수 밖에서 선언된 변수
x = 20

# 로컬변수(지역변수) : 함수 안에서 선언된 변수 a,b
# 지역변수는 함수가 종료되면 사라진다.
# 지역변수(a) : 호출항 때 전달된 값을 받을 파라미터
# 지역변수(b) : 함수 안에서 선언된 변수
def func(a):
    b = 10
    a += b
    return a

#%%
y = func(x)

print('x=', x) # x는 전역변수
print('y=', y) # y는 전역변수

#%%
# 함수 func()에 선언되어 있는 변수(a,b)에는 함수 밖에서 접근할 수 없다.

print('a=', a) # NameError: name 'a' is not defined
print('b=', b) # NameError: name 'b' is not defined



