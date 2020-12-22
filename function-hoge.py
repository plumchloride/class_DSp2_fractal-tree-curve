from turtle import *

def rect(num):
    for i in range(4):
        forward(num)
        left(90)

def five_ster(num):
    for i in range(5):
        forward(num)
        right(144)

def circle(num):
    for i in range(360):
        forward(num)
        left(1)

rect(100)
forward(150)
five_ster(100)
circle(3)

mainloop()
done()