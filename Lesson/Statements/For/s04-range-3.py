# 반복문(for)
# range(시작, 끝) 
#   - 시작부터 끝까지 연속적인 숫자를 생성

# 1부터 10까지 수에서 홀수
print("#1부터 10까지 수에서 홀수")
b = 1   # 시작값
e = 10  # 종료값
s = 2   # 증가값
for cnt in range(b,e,s): # 1,3,5,7,9
    print(cnt)

# 1부터 10까지 수에서 짝수
print("#1부터 10까지 수에서 홀수")
b = 2   # 시작값
e = 11  # 종료값
s = 2   # 증가값
for cnt in range(b,e,s): # 2,4,6,8,10
    print(cnt)

