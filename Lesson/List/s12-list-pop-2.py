# 리스트의 특정 요소를 꺼내기(pop)
# 꺼낸 요소는 삭제된다.

l = ['삼성', 'LG', 'SK', 'Apple', '현대차']
print(l)

# 특정한 위치의 요소에서 꺼냄
# 3번째 요소를 꺼냄
index = 3 # 'Apple'
value = l.pop(index)
print(l, value)

