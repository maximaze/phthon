# 예외처리
# 예외 발생시키기 : raise
# raise(메시지) : except에서 예외 메시지를 출력할 수 있다.

# NotImplementError는 Bird를 상속받은 자식 클래스에서
# fly() 메서드를 반드시 구현하도록 강제

class Bird:
    def fly(self):
        raise NotImplementedError("아직 날개가 자라지 않아 날 수 없습니다.")
        
# 예외처리
try:
    bird = Bird()
    bird.fly()
except NotImplementedError as e:
    print("[Bird] NotImplementedError:", e)
    
print("THE END")