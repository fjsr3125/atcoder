s = input()
boin = ["a", "i", "u", "e", "o"]
word = ""
for c in s:
    if c in boin:
        continue
    else:
        word += c

print(word)

