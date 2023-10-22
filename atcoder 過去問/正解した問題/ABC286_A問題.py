n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

b = a.copy()

b[p-1:q] = a[r-1:s]
b[r-1:s] = a[p-1:q]
for i in range(len(b)):
  print(b[i], end = " ")