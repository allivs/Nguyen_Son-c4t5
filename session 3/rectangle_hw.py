from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c = 1

for a in range(5):
    color(colors[c-1])
    c += 1
    begin_fill()
    forward(50)
    for i in range(2):
            right(90)
            forward(100)
            right(90)
            forward(50)
    end_fill()
mainloop()

print("cho em qua đi anh Hoà, bài này em hỏi anh Huy với anh Đức rồi mà chẳng ai giúp em cả~~")
