# 함수예제

# 파라미터 a,b를 받아서 큰 값을 리턴하는 함수
# 숫자 = Max(숫자, 숫자)

def Max(a,b):
    if a>=b:
        return a
    else:
        return b
    
print(Max(10,20))
print(Max(11,11))

#%%
# max() 함수가 내장함수로 제공되지만 사용자가 정의한 함수가 있다면
# 사용자 정의 함수를 실행한다.
def max(a,b):
    print(f"user: max({a},{b})")
    if a>=b:
        return a
    else:
        return b

print(max(99,88))

#%%

def Max(a,b):
    if a>=b:
        return f"a({a})가 b({b})보다 크다"
    if b>=a:
        return f"b({b})가 a({a})보다 크다"

print(Max(1,2))

a = 1
b = 2
print(max(a,b))
