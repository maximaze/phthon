'''
[문제7] 전자계산기 클래스(Calc)를 파이썬으로 코딩하라.
        - 메소드(add, sub, mul, div)는 숫자를 인자로 받아 누적된 값을 대상으로 연산을 수행한다.
        - add(더하기), sub(빼기), mul(곱하기), div(나누기)
        - 메소드의 파라미터는 숫자 한 개
        - 연산결과는 tot 멤버 속성에 보관한다.
'''
class Calc:
    def __init__(self):
        self.tot = 10

    def add(self, num):
        self.tot += num
        return self.tot
 
    def sub(self,num):
        self.tot -= num
        return self.tot
    
    def mul(self,num):
        self.tot *= num
        return self.tot
    
    def div(self,num):
        self.tot /= num
        return self.tot

add = Calc()
sub = Calc()
mul = Calc()
div = Calc()
print("더하기:", add.add(20))
print("빼기:", sub.sub(5))
print("곱하기:", mul.mul(4))
print("나누기:", div.div(2))


