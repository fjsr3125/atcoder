# m = int(input())
# d = list(map(int, input().split()))

# d_sum = sum(d)
# year_median = (d_sum + 1) / 2

# m_sum = 1

# for i in range(m):
#     if m_sum < year_median:
#         m_sum += d[i]
#     elif m_sum == year_median:
#         print(i+1, m_sum)
#         break
#     elif m_sum > year_median:
#         print(i,int(year_median - sum(d[:i-1]))) 
#         break
        



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