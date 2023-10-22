n = int(input())
s = [input() for _ in range(n)]

judge = "Yes"

for i in range(n):
  if s[i][0] not in  ["H" ,"D" , "C" , "S"]:
    judge = "No"
  
for i in range(n):
  if s[i][1] not in ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" ]:
    judge = "No"

for i in range(n):
  for j in range(i+1, n):
    if s[i] == s[j]:
      judge = "No"

print(judge)
    
    