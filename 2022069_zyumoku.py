from turtle import *


speed(1) #何が起きているかわかりやすいようにスピード調節

# nを変えてもきちんと動く（枝は重なるが）
def zyumoku_again(x,y,f_int,head,angle,n):
    penup()                                                     #ペンをあげる
    goto(x,y)                                                   #枝の根元に移動
    pendown()                                                   #ペンを下げる
    setheading(head)                                            #頭の角度を枝の角度とそろえる
    left(angle)                                                 #左or右に30度向く(初回のみ0度)
    forward(f_int)                                              #決められた長さだけ前に進む
    x = xcor()                                                  #移動した先のx座標の保存(次に再帰する際の根元のx座標)
    y = ycor()                                                  #移動した先のy座標の保存(次に再帰する際の根元のy座標)
    head = heading()                                            #自分の頭の位置を保存(次に再帰した際の頭の角度)
    if n > 0:                                                   #規定されている再帰の回数に達した場合終了させる
        zyumoku_again(x,y, f_int * 2/3, head, 30, n-1)          #左枝(角度30度)の作成　枝長さを2/3にして再帰回数を-1にしている
        zyumoku_again(x,y, f_int * 2/3, head, -30, n-1)         #右枝(角度-30度)の作成　枝長さを2/3にして再帰回数を-1にしている

zyumoku_again(0,-200,200,90,0,4)                               #(0,-200)の地点からはじめの枝の長さ200で絶対角度角度90度で4回枝分かれする。

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

#一応gitで管理して作成していたリポジトリのURL(https://github.com/plumchloride/class_DSp2_fractal-tree-curve)