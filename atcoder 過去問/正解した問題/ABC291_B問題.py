n = int(input())
x = list(map(int, input().split()))

x_sort = sorted(x)

x_sort_avg = (sum(x_sort[n:4*n])) / (3*n)
print(x_sort_avg)


