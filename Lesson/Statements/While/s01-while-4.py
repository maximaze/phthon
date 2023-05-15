# 반복문(while)
# while 조건식:
#   실행문
#   ...

# 반복회수를 변수에 담아서 출력하라.
count = 1
while count <= 100:  # 1,2,3,4, ... 10
    print('나무를 {0}번 찍는다.'.format(count))
    count += 1

print('count=', count)
print("THE END")