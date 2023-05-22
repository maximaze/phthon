# 예외처리
# 인덱스 오류 : IndexError
# 제로(0)으로 나누기 : ZeroDivisionError

lst = [1,3,5,2,4,]
print(lst)

try : 
    for x in lst:
        y = x / lst[x]
        print(f"x({x}) / {lst[x]} -> {y}")
except ZeroDivisionError as e:
    print("[ZeroDivisionError]",e)
except IndexError: # 아무 처리도 하지 않음)
    pass