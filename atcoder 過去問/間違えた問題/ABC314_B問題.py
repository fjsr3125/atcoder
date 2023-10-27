n = int(input())
p = []
for _ in range(n):
  c = int(input())
  a = set(map(int, input().split()))
  p.append(a)

x = int(input())

ans = []
cnt = 1000

for i in range(n):
  if x in p[i]:
    if cnt == len(p[i]):
      ans.append(i+1)
    elif cnt > len(p[i]):
      ans = [i + 1]
      cnt = len(p[i])

print(len(ans))
print(*ans)

n = int(input())
p = []
for _ in range(n):
  c = int(input())
  a = set(map(int, input().split()))
  p.append(a)

x = int(input())

ans = []
cnt = 1000

for i in range(n):
  if x in p[i]:
    if cnt == len(p[i]):
      ans.append(i+1)
    elif cnt > len(p[i]):
      ans = [i+1]
      cnt = len(p[i])

print(len(ans))
print(*ans)