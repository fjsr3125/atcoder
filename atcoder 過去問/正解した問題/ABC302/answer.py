a, b = map(int, input().split())
count = 0
def func(a, b):
    mod = a % b
    quotient = a // b
    if mod == 0:
        print(quotient)
    else:
        print(quotient + 1)

func(a, b)