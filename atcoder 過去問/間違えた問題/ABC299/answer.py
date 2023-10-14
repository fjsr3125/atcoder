n = int(input())
s = input()
count_1 = 0 #|マークを数えるためのカウンター
count_2 = 0 #*マークを数えるためのカウンター

for c in s:
    if c == "|":
        count_1 += 1
    elif c == "*":
        count_2 += 1
    else:
        continue
    
    if count_1 == 2:
        break
  
if count_2 == 1:
    print("in")
else:
    print("out")
    
