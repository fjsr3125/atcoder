N, H, X = map(int, input().split())
P_list = list(map(int, input().split()))
counter = 0
for p in P_list:
    counter += 1
    if p + H < X:
        continue
    else:
        break
print(counter)

        