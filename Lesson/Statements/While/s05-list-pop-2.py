# 반복문(while)

lst = [2,4,6,8,10]

# list.pop(0) 자료를 처음부터 하나씩 꺼냄
# 꺼낸 후 list에서는 자료가 삭제됨
while lst:
    print(lst.pop(0))

print('lst:', lst)
