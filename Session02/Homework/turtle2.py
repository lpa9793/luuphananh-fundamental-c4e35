from turtle import *
for i in range(3, 7):
    goc_bu = 360/i 
    color("red" if i%2==0 else "blue")
    if i % 2 == 0:
        color("red")
    else:
        color("blue")
    for j in range(1, i+1):
        forward(100)
        left(goc_bu)
mainloop()
#da giac deu co so do goc bang 180*(i-2)/i, goc bu bang 360/n
