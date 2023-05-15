# 딕셔너리 조사(in)

weeks = { 1:'월', 2:'화', 3:'수', 4:'목', 5:'금', 6:'토' }

print('일요일:', 0 in weeks)
print('월요일:', 1 in weeks)

key = 7
seven = key in weeks
print('key=', key, ', seven=', seven)