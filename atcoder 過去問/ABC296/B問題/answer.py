# n = list(input())
# n = n[:len(n)-1]
# n_last = n[len(n) - 1]

# if int(n_last) % 2 == 0:
#     print("Yes")
# elif sum([int(x) for x in n]) % 3 == 0:
#     print("Yes")
# else:
#     print("No")
import math
n = int(input())

n_sqrt = math.sqrt(n)



for i in range(1, int(n_sqrt)):
    if  i != 1:
        if n % i == 0 and (i % 2 != 0) and (i % 3 != 0):
             print("No")
             exit()
    else:
        continue
print("Yes")


