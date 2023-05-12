# 리스트
# 리스트안에 리스트


# 성적: 이름, [국어, 영어, 수학]
scores = ['우등생',[70,80,90]]

# 마지막 요소를 변수에 할당([70,80,90])
score = scores[-1]

# score는 scores[1]를 참조(리퍼런트) 링크
# 참조된 변수에서 값을 바꾸면 원본도 데이터도 바뀐다.
# 리스트(list)의 참조를 통해서 원본 데이터를 변경할 수 있다.
score[0] = score[1] = score[2]= 60

total = score[0] + score[1] + score[2]
average = total / 3
print('이름: ', scores[0])
print('점수: ', score)
print('총점: ', total)
print('평균: ', average)

print("원본:", scores)
