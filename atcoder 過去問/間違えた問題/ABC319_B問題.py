# n = int(input())

# list_zero = []

# list_div = []

# for i in range(n):
#   if n % (i+1) == 0 and i+1 <= 9:
#     list_div.append(i+1)

# list_div = set(list_div)

# list_div = list(list_div)

# list_div_rev = list_div[::-1]



# for i in range(n+1):
#   for j in list_div_rev:
#     min_div = 9999
#     if i % j == 0:
#       min_div = min(min_div, n//j)
#   if min_div == 9999:
#     list_zero.append("-")
#   else:
#     list_zero.append(min_div)
  
#   print(list_zero)


n = int(input())
j_list = [j for j in range(1, 10) if n % j == 0]

s = ["-"] * (n+1)
for i in range(n + 1):
  for x in j_list:
    if i % (n // x) == 0:
      s[i] = str(x)
      break

ans = "".join(s)
print(ans)


N = int(input())

j_lst = [j for j in range(1, 10) if N % j == 0]  # Nの約数のリスト
s = ['-'] * (N + 1)
for i in range(N + 1):
    for x in j_lst:
        if i % (N // x) == 0:
            s[i] = str(x)
            break
ans = ''.join(s)
print(ans)
