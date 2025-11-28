word = input()
finale_list = list()
count_letter = int()
count_word = int()
count_vowels = int()
count_unspoken = int()
len_list = list()
vowels = ["а","е","ё","и","о","у","ы","э","ю","я","a", "e", "i", "o", "u"]
unspoken = ["б","в","г","д","ж","з","й","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ","b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

word_list = list(word.split(" "))

for c in word_list:
    count_word += 1
    len_list.append(len(c))
    

for c in word.lower():
    count_letter += 1
    for v in vowels:
        if c == v:
            count_vowels += 1
    for u in unspoken:
        if c == u:
            count_unspoken += 1

max_string = max(word_list, key=len)

print(f"Word count: {count_word}\nNumber of symbols: {count_letter}\nNumber of vowels: {count_vowels}\nNumber of consonants: {count_unspoken}\nThe longest word: {max_string}")