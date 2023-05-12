# 리스트에 요소 삽입(insert)
# 리스트의 특정 위치에 요소(값)을 삽입
# 원본에 리스트의 변경 발생
# insert(pos, value) :
#  - pos : 위치
#  - value : 값
###################################################
# 잘못된 위치를 지정하더라도 에러는 발생하지 않음
# 자료는 무조건 맨 마지막에 삽입
# append()와 동일한 효과

l = ['하나', '둘']
print(l)

# 위치 1번째 즉 값('둘') 앞에 '다음'을 삽입
l.insert(1, '다음')
print(l)

# 위치 처음(0번째) 즉 값('영')을 삽입
l.insert(0, '영')
print(l)

# 마지막에 삽입(append와 같은 효과)
l.insert(len(l), '마지막')
print(l)


# 잘못된 위치를 지정하더라도 에러는 발생하지 않음
# 자료는 무조건 맨 마지막에 삽입
# append() 동일한 효과
print('갯수:', len(l))
l.insert(9, '잘못된 위치에 삽입')
print(l)

# 맨 마지막에서 첫 번째에 삽입
# 기존 마지막에 잇는 요소는 뒤로 한 칸 이동
l.insert(-1, '-1로 삽입')
print(l)

# 맨 앞 삽입
l.insert(len(l)*-1, "맨 앞으로")
print(l)

# 맨 앞 삽입
l.insert(len(l)*-1-1, "맨 앞에서 더 앞으로")
print(l)

# 리스트 뒤에 데이터 요소를 추가
l.append('THE END')
print(l)