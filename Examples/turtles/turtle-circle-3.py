# turtle: circle

import turtle

canvas = turtle.Pen()

# 문자열로 입력받은 값을 정수로 변환
# 정수 = int(문자열)
circles = int(turtle.numinput("원의 갯수", 
    "그리기를 원하는 원의 갯수를 입력하세요", 6))

for x in range(circles):
    canvas.circle(100)
    canvas.left(360 / circles)

turtle.done()    