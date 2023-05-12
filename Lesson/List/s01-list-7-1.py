# 리스트
# 리스트안에 리스트


# 성적: 이름, [국어, 영어, 수학]
scores = ['우등생',[70,80,90]]  # 2차원(행,열)
name = scores[0][0] + scores[0][1] + scores[0][2]

n1 = scores[0][0]   # '우'
n2 = scores[0][1]   # '등'
n3 = scores[0][2]   # '생'

kor  = scores[1][0]
eng  = scores[1][1]
math = scores[1][2]
total = kor + eng + math
average = total / 3
print('이름: ', scores[0], name)
print('이름: ', n1, n2, n3)
print('점수: ', scores[1])
print('국어: ', kor)
print('영어: ', eng)
print('수학: ', math)
print('총점: ', total)
print('평균: ', average)

