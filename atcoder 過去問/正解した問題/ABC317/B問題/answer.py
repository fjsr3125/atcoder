n = int(input())
a = list(map(int,input().split()))

a_sort = sorted(a)
for i in range(n-1):
    if a_sort[i] + 1 != a_sort[i+1]:
        print(a_sort[i] + 1)
        break
    else:
        continue
