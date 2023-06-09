# 딕셔너리

d = {}

# 키에 튜플 지정
tk = (1,3,5)      # 튜플
lv = [1,3,5,7,9]  # 리스트
d[tk] = lv
print(d)

print(d[tk])        # 튜플을 가지고 있는 변수
print(d[(1,3,5)])   # 튜플
print(d[1,3,5])     # 튜플

# 리스트로 조회 불가
# TypeError: unhashable type: 'list'
# print(d[[1,3,5]])     

# 리스트를 튜플로 전환하여 조회
print(d[tuple([1,3,5])])     

