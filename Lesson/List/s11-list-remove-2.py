# 리스트 요소 삭제(remove)
# 처음 찾은 값만 삭제
# list.remove(value)

# 리스트의 요소에서 해당하는 값을 찾아 삭제
# 리스의 갯수가 줄어든다.

l = ['삼성', 'LG', 'SK', 'Apple', '현대차', 'LG']
print(l)

# remove는 리스트 객체의 함수
# 리턴값이 없음
l.remove('LG')
print("remove('LG'):", l)   # 처음 찾은 값만 삭제

# 찾으려는 값이 없으면?
# ValueError : list.remove(x): x not in list
# 프로그램 종료
l.remove('IBM')
print("remove('IBM'):", l)

# 'SK'를 del를 사용하여 지우려면?
sk = l.index('SK')
del l[sk]
print('del:', l)


