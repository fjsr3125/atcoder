s = input()

s_change = ""

for c in s:
  if c == "0":
    s_change += "1"
  elif c == "1":
    s_change += "0"

print(s_change)
