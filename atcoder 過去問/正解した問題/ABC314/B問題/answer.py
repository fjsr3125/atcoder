n = int(input())
c = [0] * 101
a = [[] for _ in range(101)]

for i in range(1, n + 1):
    c[i] = int(input())
    a[i] = list(map(int, input().split()))

x = int(input())
print(n,c,a,x)