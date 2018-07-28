from turtle import *
speed(-1)
shape("turtle")

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
t = 0
for n in range(3, 7):
    color(colors[t])
    t += 1
    forward(100)
    for i in range(n-1):
        left(360/n)
        forward(100)
    left(360/n)
mainloop()

print("cho em qua đi anh Hoà, bài này em hỏi anh Huy với anh Đức rồi mà chẳng ai giúp em cả~~")