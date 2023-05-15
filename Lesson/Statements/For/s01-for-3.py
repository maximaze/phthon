# 반복문(for)
# for 변수 in 리스트, 튜플, 문자열, ...

lists = [(1,'one'), (2,'two'), (3,'three'), (4,'four')]

# 리스트에 들어 있는 내용의 갯수만큼 반복하면서
# 아이템을 하나씩 꺼내서 변수에 담아준다.
for tuples in lists: # 4번 반복
    print(type(tuples), tuples)
    print(tuples[0], ',', tuples[1])


