word = input()
word_count = 0
offers_number = 0
punctuation_number = 0

word_list = list(word.split(" "))
offers_list = list(word.split("."))
punctuation_marks = ["!",",",".","'","?","-","*","«","»"]

for w in word_list:
    word_count += 1

offers_number1 = word.count('.')
offers_number2 = word.count('!')
offers_number3 = word.count('?')
offers_number = offers_number1 + offers_number2 + offers_number3

for w in word:
    if w in punctuation_marks:
        punctuation_number += 1

print(offers_number, word_count, punctuation_number)
