# 거북이 이동 예제

# 라이브러리 사용
import turtle

# [문제] 대각을 이루는 사각형을 두 개 그려라
# 변수 tp에 turtle이 가지고 있는 펜(Pen) 객체를 얻음
# 객체 = 객체.명령()
# 객체.메소드()
# 객체.속성

tp = turtle.Pen()

distance = 100
angle = 90

tp.forward(distance)
tp.left(angle)
tp.penup()
tp.forward(distance)
tp.left(angle)
tp.pendown()
tp.forward(distance)
tp.left(angle)
tp.penup()
tp.forward(distance)

turtle.done()