# 리스트 정렬(sort)
# 오름차순: 작은값에서 큰값으로 순서대로 정렬
# 내림차순: 큰값에서 작은값으로 순서대로 정렬

# 문자열 정렬에서 첫번째 문자가 같으면 두번째 문자를 비교하며 연속적으로 비교한다.

# 문자열 정렬
l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'Eight', 'E8', 'Nine', 'ten']

print("정렬하기 전 : ",  l)

l.sort()
print("정렬한 후 : ",  l) # 대문자가 소문자보다 ASCII 값 기준으로 작다.
