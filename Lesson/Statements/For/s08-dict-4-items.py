# 반복문(for)

# 딕셔너리(dict)
contents = {'1층':'전시장', '2층':'매장', '3층':'사무실', '4층':'통제실'}

# 딕셔너리 아이템(키와 값)
# dict.items()
for item in contents.items():
    print(item, type(item))
    print('key :', item[0])
    print('value :', item[1])

print("# unpack tuple")
for item in contents.items():
    key, value = item # tuple
    print('key :', key)
    print('value :', value)




