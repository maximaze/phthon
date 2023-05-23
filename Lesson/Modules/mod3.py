# filename : mod3.py
# module name : mod3
# __name__ :
#   - 단독으로 실행될 때 : __main__
#   - 모듈로 실행될 때 : 모듈이름("mod3")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# __name__
print("[mod3.py] __name__ = ", __name__) # "__main__","mod3"

# __name__이 "__main__"인 경우만 아래 코드를 실행
if __name__ == '__main__':
    print(">>> module mod3 test <<<")
    a = 6
    b = 4

    print('add({0}, {1}) -> {2}'.format(a,b,add(a,b)))
    print('sub({0}, {1}) -> {2}'.format(a,b,sub(a,b)))


