# filename : mod4.py
# module name : mod4
# __name__ :
#   - 단독으로 실행될 때 : __main__
#   - 모듈로 실행될 때 : 모듈이름("mod4")

# 상수용
PI = 3.141592

# 클래스
class Math:
    def circlearea(self, r): # 원의넓이: PI * (반지름+반지름)
        return PI * (r ** 2) # **곱하기 2번은 제곱
        
# 함수
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# __name__
print("[mod4.py] __name__ = ", __name__) # "__main__","mod4"

# __name__이 "__main__"인 경우만 아래 코드를 실행
if __name__ == '__main__':
    print(">>> module mod4 test <<<")
    a = 6
    b = 4

    print('add({0}, {1}) -> {2}'.format(a,b,add(a,b)))
    print('sub({0}, {1}) -> {2}'.format(a,b,sub(a,b)))
    
    print("# 원의 넓이")
    print("PI = ", PI)
    math = Math()
    cirarea = math.circlearea(10)
    print("반지름이 10인 원의 넓이는?", cirarea)
    
    
    
    
    
