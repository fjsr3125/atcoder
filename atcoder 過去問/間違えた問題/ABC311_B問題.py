n, d = map(int, input().split())

T = ["o"] * d

for _ in range(n):
  s = input()
  for i in range(d):
    if s[i] == "x":
      T[i] = "x"

prev = 0
ans = 0

for t in T:
  if t == "o":
    prev +=1
    ans = max(ans, prev)
  else:
    prev = 0

print(ans)