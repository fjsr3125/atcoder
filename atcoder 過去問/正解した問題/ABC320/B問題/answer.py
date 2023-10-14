s = input()

count = []
for i in range(len(s)):
    for j in range(len(s)):
        if i <= j:
            if s[i:j] == ''.join(list(reversed(s[i:j]))):
                count.append(i)
            else:
                continue
        else:
            continue
            
print(max(count))
print(count)