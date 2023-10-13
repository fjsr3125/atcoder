s = list(map(int, input().split()))
count = 0
for i in range(0, len(s)-1):
    if s[i] <= s[i+1] and 100 <= s[i] <= 675 and s[i] % 25 == 0:
        count += 1
    else:
        break

if count == (len(s)-1):
    print("Yes")
else:
    print("No")