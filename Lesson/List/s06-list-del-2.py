# 리스트 삭제(delete)
# del 내장 함수(Built-in Function)
# del 객체
# del list[index]

a = [1,3,5]
print('a=', a, 'len(a) :', len(a))

# del a[:]
# print('a=', a, 'len(a) :', len(a))

# 삭제 효과
# del과 다른점은 새로운 리스트의 메모리가 할당
# 처리속도가 빠름
# 메모리의 사용적인 측면에서는 낭비요소
a = []
print('a=', a, 'len(a) :', len(a),",",id(a))