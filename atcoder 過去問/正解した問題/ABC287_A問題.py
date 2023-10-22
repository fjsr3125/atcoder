n = int(input())
s = [input().split() for _ in range(n)]

For_count = 0
Against_count = 0

for item in s:
  if item == ["For"]:
    For_count += 1
  elif item == ["Against"]:
    Against_count += 1

if For_count > Against_count:
  print("Yes")
else:
  print("No")
