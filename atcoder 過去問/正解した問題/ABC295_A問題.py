n = int(input())
w = list(input().split())

list = ["and", "not", "that", "you", "the"]

flag = "No"

for item in w:
  if item in list:
    flag = "Yes"
    print(flag)
    exit()
print(flag)