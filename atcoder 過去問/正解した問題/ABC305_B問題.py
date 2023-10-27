p, q = input().split()

dict = {"A":0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}

for k, v in dict.items():
  if k == p:
    p = v
  elif k == q:
    q = v

print(abs(p-q))
