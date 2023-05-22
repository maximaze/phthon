# 예외처리
# 예외 발생시키기 : raise

# NotImplementError는 Bird를 상속받은 자식 클래스에서
# fly() 메서드를 반드시 구현하도록 강제

class Bird:
    def fly(self):
        raise NotImplementedError 
        
        
bird = Bird()
bird.fly()

print("THE END")










