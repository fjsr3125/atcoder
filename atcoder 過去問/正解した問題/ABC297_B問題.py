n = input()

B_first = n.find("B")
B_last  = n.rfind("B")
R_first = n.find("R")
R_last  = n.rfind("R")
K_first = n.find("K")

if (B_first + B_last) % 2 == 1 and R_first < K_first <R_last:
  print("Yes")
else:
  print("No")
