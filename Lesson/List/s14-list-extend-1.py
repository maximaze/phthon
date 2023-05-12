# 리스트의 요소에서 요소를 추가하여 확장(extend)
# 기존에 있는 리스트에 내용을 추가하여 확장
# 다수의 append()를 하나로 처리하는 효과
# 추가되는 리스트는 개별적으로 하나씩 들어가게 된다.

l = ['삼성', 'LG', 'SK', 'Apple']
e = ['LG', '현대차', '삼성', 'LG']
print(l)
print(e)

l.extend(e)
print('l: ',l)
print('e: ',e)