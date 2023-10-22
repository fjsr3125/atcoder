n, m =map(int, input().split())
s = input()
t = input()

if (s == t[:n]) and (s == t[m-n:]):
  print(0)
elif (s == t[:n]) and (s != t[m-n:]):
  print(1)
elif (s != t[:n]) and (s == t[m-n:]):
  print(2)
elif (s != t[:n]) and (s != t[m-n:]):
  print(3)

# N, M = map(int, input().split())
# S = input()
# T = input()

# f1 = S == T[:N]  # 接頭辞ならTrue
# f2 = S == T[-N:]  # 接尾辞ならTrue
# match (f1, f2):
#     case (True, True): print(0)
#     case (True, False): print(1)
#     case (False, True): print(2)
#     case (False, False): print(3)



