word = input()
ban_word_list = list()
finale_list = list()
b = ""

while True:
    ban_word =  input()
    if ban_word == "exit":
        break
    else:
        ban_word_list.append(ban_word)

word_list = list(word.split(" "))
for w in word_list:
    w = b
    b = b.lower
    ban_word_list = ban_word_list.lower

    if b in ban_word_list:
        w = "***"
        finale_list.append(w)
    else:
        finale_list.append(w)

finale_word = " ".join(finale_list)

print(finale_word)