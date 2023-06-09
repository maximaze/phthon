# 반복문(while)
# while 문에서 break를 만나지 못하면 else 실행
# break를 만나지 않고 정상적으로 실행

# 리스트에서 자료 꺼내기
lists = [2,4,6,8,9,10]
cnt = 0
tot = 0

# 리스트에 들어 있는 값 가운데 짝수의 합
while cnt < len(lists):
    val = lists[cnt]
    if val % 2: # 홀수
        print('브레이크...')
        break
    tot += val
    print(f"[cnt={cnt}] val={val}, tot={tot}")
    cnt += 1
else:
    print('홀수가 없습니다.')    

print(f'인덱스 0부터 {cnt-1}까지의 짝수의 합은? {tot}')    

