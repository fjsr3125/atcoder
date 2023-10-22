n = int(input())
s = [input() for _ in range(n)]

victory_count = [0] * n

for i in range(n):
  for j in range(n):
    if s[i][j] == "o":
      victory_count[i] += 1
    
list = [i for i in range(n)]
victory_dict = dict(zip(list, victory_count))

sorted_dict = sorted(victory_dict.items(), key = lambda item: item[1], reverse = True)

sorted_keys = [item[0]+1 for item in sorted_dict]

for i in range(n):
  print(sorted_keys[i], end = " ")