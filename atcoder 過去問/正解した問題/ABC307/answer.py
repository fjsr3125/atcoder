import numpy as np
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(np.array_split(l, 3))
n = int(input())
a = list(map(int, input().split()))
a_split = np.array_split(a, n)
b = []
for i in range(n):
    b += sum(a_split[i])
print(b)