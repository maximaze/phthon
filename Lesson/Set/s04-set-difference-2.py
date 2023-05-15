# 셋: 차집합(difference)
# set.difference(set)

s1 = set("1234567890")
s2 = set("12468AB")

# 차집합
# s1에서 s2에 있는 데이터를 제외하고 남은 데이터를 선택
s3 = s1.difference(s2)
s4 = s1 - s2
print(s1)
print(s2)
print('result=', s3)
print('result=', s4)

#
s3 = s2.difference(s1)
s4 = s2 - s1
print(s1)
print(s2)
print('result=', s3)
print('result=', s4)
