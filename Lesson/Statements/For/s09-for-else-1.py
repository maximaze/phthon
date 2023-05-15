# 반복문(for)
# for ... else

lists = [2,4,6,8,10]
tot = 0

# for문에서 break를 발견하지 못하면 else 실행
for val in lists:
    if val % 2: # 홀수
        break
    tot += val
    print(val)
else:
    print('홀수가 없습니다.')    

print('짝수의 합:', tot)    
