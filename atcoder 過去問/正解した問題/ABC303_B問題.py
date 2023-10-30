import math
n, m = map(int, input().split())
a = [input().split() for _ in range(m)]

li = []

for i in range(m):
  for j in range(n-1):
    li.append(a[i][j:j+2])

unique_data = [sorted(sublist) for sublist in li]
unique_data = list(set(tuple(sublist) for sublist in unique_data))

unique_count = len(unique_data)
print(math.comb(n, 2) - unique_count)