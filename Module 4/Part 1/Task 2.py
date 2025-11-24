word = input()
reserv_word_list = list()
finale_list = list()

while True:
    res_word =  input()
    if res_word == "exit":
        break
    else:
        reserv_word_list.append(res_word)

word_list = list(word.split(" "))
for w in word_list:
    if w in reserv_word_list:
        w = w.upper()
        finale_list.append(w)
    else:
        finale_list.append(w)

finale_word = " ".join(finale_list)

print(finale_word)