# filename : mod2.py
# module name : mod2

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(">>> module mod2 test <<<")
a = 6
b = 4

print('add({0}, {1}) -> {2}'.format(a,b,add(a,b)))
print('sub({0}, {1}) -> {2}'.format(a,b,sub(a,b)))


