# 문자열 위치 검색(find)
#    0123456789012345678901234
a = "Python is the best choice"

# 찾는 문자열을 어떻게 연속해서 찾을 있는가?
# slicing
print(f"문자열({a})에서 문자('t')의 위치를 검색")
tcnt1 = a.find('t')
print('tcnt1=', tcnt1)
tstr = a[tcnt1+1:]
print(tstr)
tcnt2 = tstr.find('t')
print('tcnt2=', tcnt2)
print('tcnt2=', tcnt1 + tcnt2 + 1)


