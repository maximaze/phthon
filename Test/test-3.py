'''
[문제3] 다음의 내용을 파이썬으로 코딩하라.
자료형 딕셔너리(dict)를 만들어 변수 d에 할당하라
리스트 자료형으로 1,3,5값을 만들어 변수 d에 키값으로 "리스트"에 넣는다.
튜플 자료형으로 1,2,3값을 만들어 변수 d에 키값으로 "튜플"에 넣는다.
변수 d의 내용을 다음과 화면에 출력하라.
출력결과: {'리스트': [1, 3, 5], '튜플': (1, 2, 3)}
딕셔너리 변수 d를 모두 비운 후 다음과 같이 화면에 출력하라.
출력결과: 딕셔너리 변수(d) :  {}
'''

d = {
     '리스트': (1,3,5),
     '튜플': (1,2,3)
     }
print(f"'리스트:' {d['리스트']},'튜플:' {d['튜플']}")

d.clear()
print(f"딕셔너리 변수(d) : {d}")






