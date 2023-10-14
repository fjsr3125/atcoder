N = input()
flag = True
for i in range(len(N)-1):
    if int(N[i]) > int(N[i+1]):
        continue
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")

