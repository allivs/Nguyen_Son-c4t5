from turtle import *
shape("turtle")
color("green")
speed(0)

left(90)
for i in range(4):
    for i in range(2):
        left(30)
        forward(100)
        right(60)
        forward(100)
        right(150)
    right(90)

mainloop()