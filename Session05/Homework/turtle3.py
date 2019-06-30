from turtle import *
def draw_square(length,clr):
    for i in range(4):
        color(clr)
        forward(length)
        left(90)
draw_square(100,'blue')