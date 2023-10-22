n, m = map(int, input().split())
s = [input() for _ in range(n)]

# count = 0
# judge = ""
# for i in range(n):
#   for j in range(n):
#     for k in range(m):
#       if i < j:
#         if  ((s[i][k] == "o" and s[j][k] == "x") or (s[i][k] == "x" and s[j][k] == "o")):
#           judge += "o"
#         else:
#           judge += "x"
#     if set(judge) == set("o"):
#       count += 1

# print(judge)
# print(count)

res = 0
for i in range(n):
  for j in range(i+1, n):
    ok = True
    for k in range(m):
      if s[i][k] == "x" and s[j][k] == "x":
        ok = False
    if ok:
      res += 1
print(res)




