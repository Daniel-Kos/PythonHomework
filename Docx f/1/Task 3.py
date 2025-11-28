word = input()
word_count = 0
offers_count = 0
punctuation_number = 0

word_list = list(word.split(" "))
offers_list = list(word.split("."))
punctuation_marks = ["!",",",".","'","?","-","*","«","»"]

for w in word_list:
    word_count += 1

for o in offers_list:
    offers_count += 1

if offers_count > 1:
    offers_count -= 1

for w in word:
    if w in punctuation_marks:
        punctuation_number += 1

print(offers_count, word_count, punctuation_number)