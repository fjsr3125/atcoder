n = int(input())
a = list(map(int, input().split()))

ls_a = [_ for _ in range(1,n+1)]
ls = []
for i in range(n):
  if i+1 in ls:
    continue
  else:
    ls.append(a[i])

ans = set(ls_a) - set(ls)

print(len(ans))
for i in sorted(ans):
  print(i, end = " ")

