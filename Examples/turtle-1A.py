# Turtle

import turtle, random

colors = ["red", "green", "brown", "blue"]

t = turtle.Pen()

for x in range(1000):
    t.forward(x)
    t.left(90)
    t.color(random.choice(colors))