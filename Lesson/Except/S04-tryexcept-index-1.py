# 예외처리
# 인덱스 오류

lst = [2,4,6,8,10]
idx = 4

print(lst)
print(f"lst[{idx}] : {lst[idx]}")

try : 
    idx = 5
    val = lst[idx]
    # print(f"lst[{idx}] : {lst[idx]}")
    print(f"lst[{idx}] : {val}")
except IndexError as e:
    print("[IndexError]",e)