# 셋 초기값을 지정하여 생성
# 딕셔너리와 같이 중괄호({})로 감싸서 선언하지만 단일값으로 지정

lists = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
print('lists: type=', type(lists))
print('lists:', lists)

# 리스트를 셋으로 선언
weeks = set(lists)
print('weeks: type=', type(weeks))
print('weeks:', weeks)