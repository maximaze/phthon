# 거북이 이동 예제
# 라이브러리 사용
import turtle   # 터틀 라이브러리
import math     # 수학함수 라이브러리

tp = turtle.Pen()

distance = 200
angle = 90

for n in range(4):
    tp.forward(distance)
    tp.right(angle)

tp.right(45)

# x = (distance ** 2 * 2) ** 0.5 # 282
x = math.sqrt((distance ** 2) * 2)

print('x=', x)
tp.forward(x)

tp.penup()
tp.right(45 * 3) # 135도
tp.forward(distance)

tp.pendown()
tp.right(45 * 3)
tp.forward(x)

tp.penup()
tp.goto(distance / 2, -distance)
tp.pendown()
tp.right(45)
tp.circle(distance / 2)

turtle.done()