n, t = map(int, input().split())
c = [0] + list(map(int, input().split()))
r = [0] + list(map(int, input().split()))


if t in c:
  color = t
else:
  color = c[1]

ans = 0

for i in range(1, n+1):
  if c[i] == color and r[ans] < r[i]:
    ans = i

print(ans)    

    