# 리스트 정렬(sort)
# 오름차순: 작은값에서 큰값으로 순서대로 정렬(ascending)
# 내림차순: 큰값에서 작은값으로 순서대로 정렬(descending)
# 원본 데이터의 위치가 변경
# 리스트.sort() : 오름차순 정렬

lst = [1,4,3,5,9,0,99,11]
print('원본:', lst)

# 리턴값이 없다(None)
# 원본 데이터(리스트)의 위치가 변경(정렬된 형태)
# 오름차순: 숫자는 0부터 9까지 순서(작은값에서 큰값으로)
rst = lst.sort() 
print('정렬:', lst)
print('리턴:', rst) # None

# 선언과 동시에 정렬
# sort()가 리턴값이 없으므로 사용할 수가 없다.
lst = [1,4,3,5,9,0,99,11].sort()
print('lst:', lst) # None