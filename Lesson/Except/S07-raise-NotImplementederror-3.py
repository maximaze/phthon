# 예외처리
# 예외 발생시키기 : raise

# NotImplementError는 Bird를 상속받은 자식 클래스에서
# fly() 메서드를 반드시 구현하도록 강제

class Bird:
    def fly(self):
        raise NotImplementedError 

# Eagle에서 Bird를 상속받아 fly() 메소드를 재정의        
class Eagle(Bird):
    def fly(self):
        print("[Eagle] fly()")

      
eagle = Eagle()
eagle.fly()


print("THE END")









