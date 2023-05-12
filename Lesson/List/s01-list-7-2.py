# 리스트
# 리스트안에 리스트


# 성적: 이름, [국어, 영어, 수학]
scores = ['우등생',[70,80,90]]

# 행(1번째)를 변수로 할당
score = scores[1]

# 행(1번째)의 각 열에 접근
total = score[0] + score[1] + score[2] # 70, 80, 90
average = total / 3
print('이름: ', scores[0])
print('점수: ', score)
print('총점: ', total)
print('평균: ', average)

