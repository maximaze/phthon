# 예외처리
# 인덱스 오류 : IndexError
# 제로(0)으로 나누기 : ZeroDivisionError

lst = [1,5,0,2,4,]
print(lst)

try : 
    for x in lst:
        y = x / lst[x]
        print(f"x({x}) / {lst[x]} -> {y}")
except (ZeroDivisionError,IndexError) as e:
    print("[예외발생]",e)

print("[작업종료]")

# [문제]
# 예외가 발생해도 작업을 종료하지 않고 다음 처리를 계속하라.
print("[문제]")    
for x in lst:
    try:
        y = x / lst[x]
        print(f"x({x}) / {lst[x]} -> {y}")
    except (ZeroDivisionError, IndexError) as e:
        print(f"[예외발생] x({x}), {e}")
        

print("[작업종료]")    

# 작업결과
"""
x(1) / 5 -> 0.2
[예외발생] x(5), list index out of range
x(0) / 1 -> 0.0
[예외발생] x(2), division by zero
x(4) / 4 -> 1.0
"""
