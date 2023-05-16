# 거북이 이동 예제

# 라이브러리 사용
import turtle

# 변수 tp에 turtle이 가지고 있는 펜(Pen) 객체를 얻음
tp = turtle.Pen()

distance = 200
angle = 90

tp.forward(distance)

tp.left(angle)
tp.forward(distance)

tp.left(angle)
tp.forward(distance)

tp.left(angle)
tp.forward(distance)

turtle.done()