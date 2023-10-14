n = int(input())
s = input()

def func(n,s):
    count_o = 0
    count_  = 0
    count_x = 0
    for i in range(n):
        if s[i] == "o":
            count_o += 1
        elif s[i] == "-":
            count_ += 1
        elif s[i] == "x":
            count_x += 1
    if count_o != 0 and count_x == 0:
        print("Yes")
    else:
        print("No")

func(n, s)