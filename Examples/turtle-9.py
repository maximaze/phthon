from turtle import *
from random import randint

speed(0) # speed to draw to color
pensize(10) # size of the pen

colormode(255) # colormode should be 255 to show every type of color
 
# To display the color continuously the while loop is true
while True:
    # randint will have random color based on every randint the color will be called
    color(randint(0, 255), randint(0, 255), randint(0, 255))
    # it will begin to fill the circle with color
    begin_fill()
    # generate circle
    circle(20)
    # it will end to fill color
    end_fill()
    # it will start to draw
    penup()
    # x axis and y axis
    goto(randint(-500, 500), randint(-300, 270))
    # it wil stop to draw
    pendown()