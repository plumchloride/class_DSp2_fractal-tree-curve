from turtle import *

f = 200

left(90)
forward(-200)
forward(200)



def zyumoku_again(f_int,angle,n):
    left(angle)
    forward(f_int)
    forward(-f_int)
    left(-angle)
    if n > 0:
        zyumoku_again(f_int*2/3,angle,n-1)
        zyumoku_again(f_int*2/3,-angle,n-1)

zyumoku_again(f*2/3,30,4)

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

# zyumoku(f,0,0,1)

# mainloop()
# done()