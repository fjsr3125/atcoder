s = input()

s_change = ""
for i in range(0,(len(s)) - 1,2):
  s_change += s[i+1] + s[i]

print(s_change)