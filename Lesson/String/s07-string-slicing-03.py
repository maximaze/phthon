# 문자열 슬라이싱(Slicing)
# 문자열의 위치를 참조를 통해서 특정한 범위의 문자열을 추출
# 추출된 문자열은 새로운 변수를 할당하며 원본의 변화는 없다.
#############################################################
# 문자열[시작번호:끝번호]
# 시작위치: 0부터 시작
# 종료위치: 마지막값 - 1

s = "0123456789"
print(s)

# 시작번호가 0이면 생략 가능(0~4)
c = s[:5]
print(c)

