n, q = map(int, input().split())
xy = [map(int, input().split()) for _ in range(q)]
x, y = [list(i) for i in zip(*xy)]

li = [0] * (n+1)

for i in range(q):
  if x[i] == 1:
    li[y[i]] += 1 
  elif x[i] == 2:
    li[y[i]] += 2
  elif x[i] == 3:
    if li[y[i]] >= 2:
      print("Yes")
    else:
      print("No")
  
