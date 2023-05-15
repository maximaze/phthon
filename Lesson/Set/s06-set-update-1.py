# 셋에 여러 개의 데이터를 추가
# update

s1 = set([1,2,3])

print(s1)
# add(list) 지원하지 않음
# s1.add([5,6])

# s1에 리스트를 추가하여 결합
s1.update([5,6]) 
print(s1)

# s1에 셋을 추가하여 결합
s1.update({7,8})
print(s1)


#s1.add(9)와 같다.
s1.update({9})
print(s1)

# 이미 동일한 데이터가 존재하면 들어가지 않는다.
s1.add(9)
print(s1)

# 존재하지 않으면 추가됨
s1.add(0)
print(s1)

