x = 200
def decrease(num):
    if num < 0:
        return
    else:
        print(num)
        decrease(num - 1)

decrease(x)