n,d = map(int, input().split())
t = list(map(int, input().split()))

def func(n,d,t):
    count = 0
    for i in range(n-1):
        if t[i + 1] - t[i] <= d:
            print(t[i+1])
            count += 1
            break
        else:
            continue
    if count != 1:
        print(-1)
        
func(n,d,t)