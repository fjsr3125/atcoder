n = int(input())
s = input()
t = input()
count = 0
for i in range(n):
    if s[i] == t[i] or ((s[i] == "1" and t[i] == "l") or (s[i] == "l" and t[i] == "1")) or ((s[i] == "0" and t[i] == "o") or (s[i] == "o" and t[i] == "0")) :
        count += 1
        continue
    else:
        break
    
if count == n:
    print("Yes")
else:
    print("No")