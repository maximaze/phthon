# 리스트
# 리스트안에 리스트


# 성적: 이름, [국어, 영어, 수학]
scores = ['우등생',[70,80,90]]

# 마지막 요소를 변수에 할당([70,80,90])
score = scores[-1]

total = score[0] + score[1] + score[2]
average = total / 3
print('이름: ', scores[0])
print('점수: ', score)
print('총점: ', total)
print('평균: ', average)

