# 리스트 요소 추가(append)
# 기존의 리스트에 요소를 추가
# 기존의 요소의 끝에 추가

lst = []
print(lst)

lst.append([9,8,7])
lst.append([6,5,4])
print(lst)
print('length:', len(lst))

print('1차원 형태로 참조:' ,lst[1])

print('2차원 형태로 참조:')
print(lst[1][0])
print(lst[1][1])
print(lst[1][2])