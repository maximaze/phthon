'''
[문제1] 아래의 성적을 처리하는 내용을 파이썬으로 코딩하라.
국어 70점, 영어 80점, 수학 90점이다.
각 점수를 리스트 자료형(list)에 넣어라
총점을 계산하여 변수 total에 넣어라
평균을 계산하여 변수 average에 넣어라
그리고 결과를 아래와 같이 화면에 출력하라
점수:  [70, 80, 90]
총점:  240
평균:  80.0
'''

score = [70,80,90]
total = 0

print(score, type(score))
print('국어:',score[0],'점')
print('영어:',score[1],'점')
print('수학:',score[2],'점')

for s in score:
    total += s

print(f"총점={total}, 평균={total/len(score)}") 



