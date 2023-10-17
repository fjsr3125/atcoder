n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))

sara_cost = {}
#皿の色と値段を一致させる．
for i in range(0, m):
  sara_cost.update({d[i] : p[i + 1]})

cost = 0

for item in c:
  if item not in d:
    cost += p[0]
  else:
    cost += sara_cost[item]

print(cost)
