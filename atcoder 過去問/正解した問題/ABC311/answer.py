n = int(input())
s = input()
character_list = []
count = 0
for c in s:
    character_list += c
    character_set = set(character_list)
    count += 1
    if character_set == set(["A", "B", "C"]):
        break
    else:
        continue
print(count)


