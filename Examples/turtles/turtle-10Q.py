# 거북이 이동 예제
# 라이브러리 사용
import turtle


tp = turtle.Pen()

distance = 200
angle = 90

for n in range(4):
    tp.forward(distance)
    tp.right(angle)

tp.right(45)
x = (distance ** 2 * 2) ** 0.5 # 141
print('x=', x)
tp.forward(x)

tp.penup()
tp.right(45 * 3)
tp.forward(distance)
tp.pendown()
tp.right(45 * 3)
tp.forward(x)

turtle.done()