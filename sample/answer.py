n = int(input())
s = [input().split() for _ in range(n)]

list = []

for player_No in s:
  count_o = 0
  for item in player_No:
    if item == "o":
      count_o += 1
  list.append(count_o)

for item in s:
  for i in item:
    print(i)

print(list)

