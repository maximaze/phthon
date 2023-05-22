# 예외처리
# 인덱스 오류

lst = [2,4,6,8,10]
idx = 4

print(lst)
print(f"lst[{idx}] : {lst[idx]}")

idx = 5
# IndexError: list index out of range
print(f"lst[{idx}] : {lst[idx]}")





