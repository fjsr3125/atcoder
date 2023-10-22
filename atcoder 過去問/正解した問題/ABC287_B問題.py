n , m = map(int, input().split())

s = [input() for _ in range(n)]
t = [input() for _ in range(m)]

ans = 0

for i in range(n):
  for j in t:
     if s[i][3:] == j:
        ans += 1
        break

print(ans)
        


