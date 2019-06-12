# A square

from turtle import *
shape("turtle")
for i in range(100):
    forward(180)
    left(90)
    forward(180)
    left(90)
    forward(180)
    left(90)
    forward(0)

# An equilateral triangle

from turtle import *
shape("turtle")
for i in range(100):
    forward(180)
    left(120)
    forward(180)
    left(120)
    forward(0)

# A circle

from turtle import *
shape("turtle")
for i in range(100):
    circle(60)

# Multiple circles

from turtle import *
shape("turtle")
for i in range(100):
    circle(80)
    left(10)
    speed(10)
