n = int(input())
a = [input().split() for _ in range(n)]
b = [input().split() for _ in range(n)]

# flag = "No"
for i in range(n):
  for j in range(n):
    if all(a[n+1-j][i] == b[i][j]):
      print("Yes")
print("No")
