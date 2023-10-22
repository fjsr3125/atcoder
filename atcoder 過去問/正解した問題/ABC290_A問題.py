n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

test_score = 0

for i in b:
  test_score += a[i-1]

print(test_score)