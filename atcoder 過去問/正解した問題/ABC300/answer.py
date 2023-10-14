n, a, b = map(int, input().split())
c = list(map(int, input().split()))
def func(n,a,b,c):
    ab = a + b
    for i in range(n):
        if c[i] == ab:
            print(i+1)
            break
        else:
            continue
        
func(n, a, b, c)
            
