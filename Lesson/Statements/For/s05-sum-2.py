# 반복문(for)
# range(시작, 끝) 
#   - 시작부터 끝까지 연속적인 숫자를 생성

# 1부터 10까지 합
s = 1       # 시작값
n = 10      # 종료값
l = n + 1   # 지정값 = 종료값 + 1
sum = 0
for cnt in range(s, l):
    sum += cnt
    print(f"cnt={cnt}, sum={sum}")

print('sum=', sum)    
