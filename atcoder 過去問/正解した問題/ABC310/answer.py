n, p, q = map(int, input().split())
d_list = list(map(int, input().split()))
d_list_min = min(d_list)
if d_list_min + q <= p:
    print(d_list_min + q)
else:
    print(p)


