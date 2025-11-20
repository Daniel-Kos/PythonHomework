word = input()
united_word = ""
rev_united_word = ""

for w in word:
    if w == " ":
        w = ""

    united_word = united_word + w

united_word = united_word.lower()
rev_united_word = united_word[::-1]

if united_word == rev_united_word:
    print("palindrome")
else:
    print("no palindrome")