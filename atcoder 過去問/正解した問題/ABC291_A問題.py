s = input()

count = 0
for c in s:
  count += 1
  if c.isupper():
    print(count)
    exit()