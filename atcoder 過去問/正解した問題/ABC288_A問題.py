n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a,b = [list(_) for _ in zip(*ab)]

for i in range(n):
  print(a[i] + b[i])
