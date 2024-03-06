def Check(n):
    for i in range(1, n+1):
        if (i)%3 == 0:
            print("(」・ω・)」うー!",end='')
        if (i)%5 == 0:
            print("(/・ω・)/にゃー!",end='')
        if (i)%3 != 0 and (i)%5 != 0:
            print(i,end='')
        print("")

while (1):
    Temp = input("輸入數字 n = ")
    try:
        Num = float(Temp)
        if Num.is_integer():
            Check(int(Num))
            break
        else:
            print("輸入不是整數，請重新輸入")
    except:
        print("輸入不是數字，請重新輸入")
    