from turtle import *


speed(1) #何が起きているかわかりやすいようにスピード調節

# nを変えてもきちんと動く（枝は重なるが）
def zyumoku_again(x,y,f_int,head,angle,n):
    penup()
    goto(x,y)
    pendown()
    setheading(head)
    left(angle)
    forward(f_int)
    x = xcor()
    y = ycor()
    head = heading()
    if n > 0:
        zyumoku_again(x,y,f_int*2/3,head,30,n-1)
        zyumoku_again(x,y,f_int*2/3,head,-30,n-1)

zyumoku_again(0,-200,200,60,30,4)

mainloop()
done()


# 再帰関数のことがよくわからなかったが、とりあえず試行錯誤した物
# さすがにこれは再帰関数とは呼べないのでは？ 
def zyumoku(num,count,ri_count,husa):
    if count == 5:
        if ri_count == 0:
            num = back(num)
            right(90)
            zyumoku(num,count-1,ri_count+1,husa)
        elif ri_count == 1:
            if husa == 3:
                for i in range(1):
                    num = back(num)
                    left(30)
                num = back(num)
                right(90)
                zyumoku(num,count-2,ri_count - 1,husa+1)
            elif husa == 4:
                for i in range(3):
                    num = back(num)
                    left(30)
                num = back(num)
                right(90)
                zyumoku(num,count-4,ri_count - 1,1)
            for i in range(husa):
                num = back(num)
                left(30)
            num = back(num)
            right(90)
            husa += 1
            zyumoku(num,count-husa,ri_count - 1,husa)

    else:
        left(30)
        forward(num)
        zyumoku(num * 2 / 3,count + 1, ri_count,husa)

def back(a):
    a*=3/2
    forward(-a)
    return a

#left(90)
# penup()
# forward(-200)
# pendown()
# right(30)
# zyumoku(200,0,0,1)

# mainloop()
# done()