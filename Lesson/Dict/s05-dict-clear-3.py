# 딕셔너리
# 전체 지우기
# dict.clear()

d = {}

d['홀수'] = [1,3,5] # 리스트값
d['짝수'] = [2,4,6] # 리스트값
d['숫자'] = (1,2,3) # 튜플값
print(d)
print('처음:', id(d))

d.clear()
print('지움:', id(d))

d = {}
print('대입:', id(d))
