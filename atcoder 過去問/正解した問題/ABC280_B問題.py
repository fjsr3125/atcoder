n = int(input())
s = list(map(int, input().split()))

a =[0] * n

for i in range(n):
  if i == 0:
    a[i] = s[i]
  elif i >= 1:
    a[i] = s[i] - s[i-1]

for i in a:
  print(i, end = " ")