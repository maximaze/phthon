# 튜플을 리스트로 변환
# 리스트 튜플로 변환
# 원래의 자료형이 변환된 것이 아니라 새로운 자료에 기존의 이름을 붙인 것이다.

# 리스트를 튜플로 변환
t1 = tuple([1,3,4,5])
print('t1:', type(t1), t1, len(t1))

l1 = [1,3,4,5]
t2 = tuple(l1)
print('t2:', type(t2), t2, len(t2))