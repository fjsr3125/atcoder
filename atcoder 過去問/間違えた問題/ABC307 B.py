n = int(input())
s = [input() for i in range(n)]

ans = "No"
#iとjが違うときに2つの文字をくっつけて，hakoに格納する
for i in range(n):
  for j in range(n):
    if i != j:
      t = s[i] + s[j]
      for k in range(len(t)):
        if t[k] != t[-k-1]:
          flag = False
      if flag:
        ans = "Yes"



# flag = "No"

# #n(n-1) / 2 通りの組み合わせになるので，それに対してforループを回す
# for item in hako:
#   if item[:] == item[::-1]:
#     flag = "Yes"
#     print(flag)
#     # exit()
# print(flag)
