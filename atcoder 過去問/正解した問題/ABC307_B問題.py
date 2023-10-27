n = int(input())
s = [input() for _ in range(n)]

ans = "No"

for i in range(n):
  for j in range(n):
    if i != j:
        t = s[i] + s[j]
        if t == t[::-1]:
            ans = "Yes"
            print(ans)
            exit()

print(ans)

