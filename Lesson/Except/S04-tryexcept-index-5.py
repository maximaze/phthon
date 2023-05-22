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