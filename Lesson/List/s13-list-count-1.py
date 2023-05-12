# 리스트의 요소에서 해당한 값을 포함하는 갯수 세기(count)
# 객체.함수(인자)
# 리스트객체.갯수를세는함수(값)
# count = list.count(value)
# 리턴 : 일치한ㄴ 갯수 또는 없으면 ZERO(0)

l = ['삼성', 'LG', 'SK', 'Apple', 'LG', '현대차', '삼성', 'LG']
print(l)

value = 'LG'
count = l.count(value)
print(value, ':', count)

print('IBM?',l.count('IBM'))