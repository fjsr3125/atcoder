s = input()

s_change = ""
for i in range(0,len(s)/2 - 1,2):
  s_change += reversed(s[i] + s[i+1]) 
print(s_change)