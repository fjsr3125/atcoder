n, k = map(int, input().split())
a = input()

rank = ""
count = 0

for i in a:
  if i == "o":
    count += 1
    if count <= k:
      rank += i
    elif count >= k+1:
      rank += "x"
  elif i == "x":
    rank += "x"

print(rank)
