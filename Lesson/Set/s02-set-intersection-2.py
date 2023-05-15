# 셋: 교집합(intersection)

s1 = set("0123456789")
s2 = set("2468A")
print(s1)
print(s2)

# 교집합(&)
# 양쪽에 존재하는 값
s3 = s1.intersection(s2)
print('s3:', s3)

s4 = s2.intersection(s1)
print('S4:', s4)