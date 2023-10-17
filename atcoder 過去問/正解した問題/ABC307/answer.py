n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
  ans.append(sum(a[7*i:7*i+7]))

for item in ans:
  print(item, end = " ")