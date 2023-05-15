# 셋 초기값을 지정하여 생성

# 딕셔너리
dicts = {0:'Sun', 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat'}
print('dicts: type=', type(dicts))
print('dicts:', dicts)

# 딕셔너리를 셋으로 선언(키값만 취함)
# weeks = set(dicts)
weeks = set(dicts.keys())
print('weeks: type=', type(weeks))
print('weeks:', weeks)

# 딕셔너리의 값을 취하여 셋(set)으로 변환
weeks = set(dicts.values())
print('weeks: type=', type(weeks))
print('weeks:', weeks)

# 딕셔너리의 키와 값을 한 쌍으로 하는 튜플을 리스트로 한 값을 셋으로 변환
weeks = set(dicts.items())
print('weeks: type=', type(weeks))
print('weeks:', weeks)

# 순서가 없기 때문에 인덱스를 통해서 접근하면
# 항상 같은 값을 참조하는 것을 보장하지 않음
# TypeError: 'set' object is not subscriptable
# print(weeks[0])

# set -> list 변환 후 인덱스로 참조 가능
weeks_list = list(weeks)
print('weeks_list : ', weeks_list)
print('weeks_list[0] : ', weeks_list[0])
print('type(weeks_list[0]) : ', type(weeks_list[0]))