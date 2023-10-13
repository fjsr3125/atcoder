a, b = map(int, input().split())
ra, ca = (a-1) // 3, (a-1) % 3
rb, cb = (b-1) // 3, (b-1) % 3
if ra == rb and ca+1 == cb:
    print("Yes")
else:
    print("No")
