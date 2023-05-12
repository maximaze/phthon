# 리스트 인덱스(index)
# 리스트의 요소의 값을 찾아서 요소의 위치를 리턴
# 찾지 못하면 종료 : ValueError: value is not in list

a = ['one', 'two', 'three',10,'20', 'four', 'five',[10,'20'],30]

print(a)

# value : 리스트에서 찾고자 하는 값
# index : 리스트에서 value가 위치하는 인덱스
# found : 인덱스를 통해서 값을 찾았는지 유무(True or False)
value = [10, '20']
index = a.index(value)
found = (value == a[index])

print('value : ', value)
print('index : ', index)
print('found : ', found)
