n = int(input())
s = list(input())

s.insert(0,"0")

li = [0] * (n+1)

for i in range(1,n+1):
  l = 0
  for j in range(1, n-i+1):
    if s[j] != s[j + i]:
      l += 1
    else:
      break
  li[i] += l

for i in li[1:n]:
  print(i)


