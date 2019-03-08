import turtle
import math
import random as  r
t = turtle.Pen()
t.speed(2000)
t.width(5)

x1 = 0
y1 = 200
x2 = 231
y2 = -200
x3 = -231
y3 = -200
xy1 = turtle.Vec2D(x1,y1)
xy2 = turtle.Vec2D(x2,y2)
xy3 = turtle.Vec2D(x3,y3)

#it doesnt work fix
#im trying to make the tri force fractal thing
for x in range(0,10):
    pos = r.randint(1,3)
    t.pu()
    if pos == 1:
        trav = xy1 - t.pos()
    elif pos == 2:
        trav = xy2 - t.pos()
    elif pos == 3:
        trav = xy3 - t.pos()
    trav = trav * .5
    t.goto(trav)
    t.pd
    t.circle(1)

