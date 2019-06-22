from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(3, 8): 
    goc_bu = 360/i
    color(colors[i-3])
    for j in range(1, i+1):
        forward(100)
        left(goc_bu)
mainloop()
