# 예외처리
# 인덱스 오류 : IndexError

lst = [1,3,0,2,4,]
print(lst)

try : 
    for x in lst:
        y = x / lst[x]
        print(f"x({x}) / {lst[x]} -> {y}")
except IndexError as e:
    print("[IndexError]",e)
except: # 맨 마지막에 기술
    print("[예외처리] 알수 없는 오류 발생")