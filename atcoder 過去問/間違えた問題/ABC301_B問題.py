n = int(input())
a = list(map(int, input().split()))

for i in range(n-1):
  if abs(a[i] - a[i+1]) == 1:
    continue
  else:
    if a[i] < a[i+1]:
      a[i:i] = [_ for _ in range(a[i] + 1, a[i+1] - 1)]
    elif a[i] > a[i+1]:
      a[i:i] = [_ for _ in range(a[i]-1, a[i+1]+1, -1)]

for _ in a:
  print(_, end = " ")

