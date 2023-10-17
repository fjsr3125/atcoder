n, l = map(int, input().split())
a = [int(input()).split() for l in range(n)]
for i in range(n):
    for j in range(l):
        sum_ij = sum(a[i]) + a[i,j]
