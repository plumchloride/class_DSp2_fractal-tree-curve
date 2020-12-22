from turtle import *
f = 200
left(90)
penup()
forward(-200)
pendown()
right(30)

def zyumoku(num,count,ri_count):
    if count == 5:
        if ri_count == 0:
            num *= 3/2
            forward(-num)
            right(90)
            zyumoku(num,count-1,ri_count+1)  

    else:
        left(30)
        forward(num)
        zyumoku(num * 2 / 3,count + 1, ri_count, ri_count_2)
    
zyumoku(f,0,0)
# forward(f)
# left(20)
# forward(f*2/3)
# left(20)
# forward(f*4/9)
# left(20)
# forward(f*8/27)
# left(20)
# forward(f*16/81)


mainloop()
done()