n, x = map(int, input().split())
a = list(map(int, input().split()))
a_sort = sorted(a)

b = x - sum(a_sort[1:n-2])

if sum(a_sort[:n-2]) < x:
    a_sort.append(b)
    a_sort2 = sorted(a_sort)
elif sum(a_sort[:n-2]) == x:
    b = 0
    a_sort.append(b)
    a_sort2 = sorted(a_sort)

if sum(a_sort2[1:n-1]) >= x:
    print(b)
else:
    print(-1)
    


