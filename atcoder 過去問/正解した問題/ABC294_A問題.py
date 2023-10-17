n = int(input())
a = list(map(int, input().split()))

#空のリストを作成
list = []

#aから要素を取り出してきて，偶数だったら，空のリストに加える．
for item in a:
  if item % 2 == 0:
    list.append(item)
  else:
    continue

for  c in list:
  print(c, end = " ")
