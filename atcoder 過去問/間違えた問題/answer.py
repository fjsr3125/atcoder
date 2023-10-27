m = int(input())
d = list(map(int,input().split()))

tot = 0
for x in d:
    tot += x

mid = (tot+1) // 2

for i in range(m):
    if mid <= d[i]:
        print(str(i+1) + " " +str(mid))
        exit()
    else:
        mid -= d[i]
