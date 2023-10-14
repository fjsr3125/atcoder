import math
n =  int(input())
s = input()

def func(n,s):
    count_t = 0
    count_a = 0
    x = n / 2
    y = math.ceil(x)
    for c in s:
        if c == "T":
            count_t += 1
        else:
            count_a += 1
        if count_t >= y:
            print("T")
            break
        elif count_a >= y:
            print("A")
            break
  
func(n,s)