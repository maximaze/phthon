'''
[문제8] 위 문제7의 클래스(Calc)를 상속받아 처리하는 
        클래스(Calculator)를 파이썬으로 코딩하라.
        - 메소드(total)는 누적된 값을 리턴한다.
        - 메소드(average)는 누적된 값의 평균을 구한다.
        - 평균은 메소드(add, sub, mul, div)의 총 호출(수행) 횟수이다.
'''  
class Calc:
    def __init__(self, init):
        self.total = init
        
    def printtotal(self):
        print("총 계산결과:", self.total)
        return self.total  
      
class Calculator(Calc):        
    def add(self, num):
        self.total += num
        return self.total
    
    def sub(self,num):
        self.total -= num
        return self.total
    
    def mul(self,num):
        self.total *= num
        return self.total
    
    def div(self,num):
        self.total /= num
        return self.total

calc = Calculator(10)
print("더하기:", calc.add(20))
print("빼기:", calc.sub(5))
print("곱하기:", calc.mul(4))
print("나누기:", calc.div(2))




calc.printtotal()




        