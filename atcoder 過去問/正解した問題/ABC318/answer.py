n,m,p = map(int, input().split())
day = m
count = 0
while day <= n:
    day += p
    count += 1
print(count)
