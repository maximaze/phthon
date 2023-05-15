# 반복문(while)


# [문제]
# 반복문(while)을 사용하여 1부터 100까지 합을 구하라.

cnt = 1     # 증가값
sum = 0     # 합

while cnt <= 10:    # 1,2,3, .... 9, 10
    sum += cnt
    print(f'cnt={cnt}, sum={sum}')
    cnt += 1

print('합은?', sum)