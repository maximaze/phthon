# 반복문(while)


# 리스트에서 자료 꺼내기
lists = [2,4,6,8,10]
cnt = 0
tot = 0

# lists에 있는 자료를 하나씩 꺼내서 각 요소의 합을 구함
# 꺼낸 내용이 사라지지 않음(보존)
while cnt < len(lists):
    val = lists[cnt]
    tot += val
    print(f"[cnt={cnt}] val={val}, tot={tot}")
    cnt += 1

print(f'lists={lists}')    
print(f'tot={tot}')    

