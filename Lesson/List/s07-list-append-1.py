# 리스트 요소 추가(append)
# 기존의 리스트에 요소를 추가
# 기존의 요소의 끝에 추가

lst = []
print('빈 리스트(lst)', lst)

lst.append(9)
lst.append(8)
lst.append(7)

print('append : ', lst)

# 한번에 리스트 항목 [6,5,4] 을 추가
lst.append( [6,5,4] )   # 리스트 항목 하나를 추가
print('append([6,5,4]) : ', lst)

# 여러 항목을 나열식으로 추가할 수 없다.
# 반드시 한 개의 요소만 추가할 수 있다.
# TypeError: append() takes exactly one argument (3 given)
# lst.append(3,2,1)
# print('append([6,5,4]) : ', lst)

# 다양한 자료형을 추가할 수 있다.
# 하나의 문자열은 하나의 요소로 추가할 수 있다.
lst.append('end')
print("append('end') : ", lst)

print("length : ", len(lst))
