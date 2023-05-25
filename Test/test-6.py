'''
[문제6] 입력받은 인자의 모든 값을 더하는 
        총합을 리턴하는 함수를 파이썬으로 코딩하라. 
        - 함수의 인자는 가변인자로 처리하라.
'''

def tot(*args):
    total = 0
    
    for x in args:
        total += x
    return total

tot1 = tot(1,2,3,4,5)
print('총합:' ,tot1)




