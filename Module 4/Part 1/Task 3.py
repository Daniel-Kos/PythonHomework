word = input("Enter a word: ")
num = 0

for w in word:
    if w == ".":
        num += 1
    else:
        continue

print(num)