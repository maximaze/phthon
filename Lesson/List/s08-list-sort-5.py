# 리스트 정렬(sort)
# 오름차순: 작은값에서 큰값으로 순서대로 정렬
# 내림차순: 큰값에서 작은값으로 순서대로 정렬
#   - 소트(sort)를 한 후 뒤집기(reverse)하면 내림차순 효과를 낼 수 있다.
#   - list.sort -> list.reverse()
#   - 소트(sort)를 한 후 뒤에서부터 역으로 참조, 소트 후 원본의 변화는 없다.
# 문자열 정렬(내림차순)
l = ["one","two",4,7]

print(l)

# 자료형이 다른 경우에는 정렬(sort)를 할 수 없다.
# 값을 비교할 수 없다.
# TypeError: '<' not supperted between instances of 'int' and 'str'
# l.sotr()

b1 = "one" < "two"
print(b1)

# 자료형이 다르면 비교를 할 수 없다.
# TypeError: '<' not supperted between instances of 'int' and 'str'
# b2 = "one" < 123
# print(b2)