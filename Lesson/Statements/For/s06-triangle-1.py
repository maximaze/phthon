# 반복문(for)

# [문제]
# 1부터 10까지 증가하면서 *를 동일한 라인에 출력
'''
1:*
2:**
3:***
4:****
5:*****
...
'''

for x in range(1,11):
    print(x, end=':')
    for y in range(x):
        print('*', end='')
    print()


