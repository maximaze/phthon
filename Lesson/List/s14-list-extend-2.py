# 리스트의 요소에서 요소를 추가하여 확장(extend)
# 기존에 있는 리스트에 내용을 추가하여 확장
# 다수의 append()를 하나로 처리하는 효과

l = ['삼성', 'LG', 'SK', 'Apple']
e = ['LG', '현대차', '삼성', 'LG']
print(l)
print(e)

# extend()와 append()는 차이가 있다.
l.append(e)
print(l)
