'''
[문제10] 외부함수에서 내부함수를 동적으로 생성하여
        리턴하는 함수를 정의하여 실행하는 코드를 코딩하라.
'''

def pump(name, *args):
    print(f"name({name})")
    
    def score():
        max = -1;
        for val in args:
            if max == -1 or val > max:
                max = val
        return max
    return score

t1 = pump("여름아 부탁해",20,100,70)
print('최고점수:' ,t1())





