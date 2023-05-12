# 튜플: 슬라이싱


t = (1,3,5,7,9)
print(t)

# 원본 데이터에는 변확 없다.
# 슬라이싱 한 데이터를 새로 만들어 리턴
# tuple[start:end]
# index : start ~ (end - 1)
t24 = t[2:4]
print('t :', t)
print('t[2:4] :', t24)

print('처음부터 끝까지: ', t[:])
print('처음부터 2까지: ', t[:2])
print('2부터 끝까지: ', t[2:])

# 아래 두 경우는 어떤차이가 있는가?
# 같은 메모리를 공유
print('t:',t,id(t))
t1 = t
print('t1:', t1,id(t1))

t2 = t[:]
print('t2:', t2,id(t2))

t3 = t[0:]
print('t3:', t3,id(t3))

# 원래 참조하고 있는 메모리를 버리고
# 새로운 튜플의 메모리를 할당 받으므로
# 원본의 변화는 없다.
t3 = (10,11,)
print('t: ',t,id(t))
print('t3: ',t3,id(t3))

# 튜플을 인덱스를 통해서 값을 바꿀수 없으므로
# 같은 메모리를 참조해도 문제가 없다.
# TypeError: 'tuple' object does not support item assignment
# t2[0]= t3[0] = 99

################################################
# list와 tuple의 slice 차이?
print('# list와 tuple의 slice 차이?')
ls = [1,3,5,7,9]
l1 = ls
l2 = ls[:]
l3 = ls[0:]
l2[0] = l3[0] = 99
print('ls: ',ls,id(ls))
print('l1: ',l1,id(l1))
print('l2: ',l2,id(l2))
print('l3: ',l3,id(l3))


