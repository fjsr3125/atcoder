n = int(input())
list = []
for i in range(n):
  a,b = input().split()
  list.append([a, int(b)])

min_value  = 10 ** 18
for i in range(n):
  if list[i][1] < min_value:
    min_value = list[i][1]
  else:
    continue

for i in range(min_value,n):
  print(list[i][0])
for i in range():
  a