'''
[문제4] 다음의 내용을 파이썬으로 코딩하라.
집합(set) 자료형으로 1,3,5,7,9값을 만들어 변수 s1 할당한다.
집합(set) 자료형으로 1,2,4,6,8값을 만들어 변수 s2 할당한다.
변수 s1과 s2를 합집합을 하여 변수 s3에 할당한다.
변수 s1,s2,s3를 화면에 다음과 같이 출력한다.
출력결과:
s1: {'3', '7', '1', '5', '9'}
s2: {'2', '6', '1', '4', '8'}
s3: {'3', '2', '7', '6', '1', '4', '5', '9', '8'}
'''

s1 = set({1,3,5,7,9})
s2 = set({1,2,4,6,8})
s3 = s1 | s2

print(s1)
print(s2)
print(s3)




