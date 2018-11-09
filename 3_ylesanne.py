word_reverse = ""

def reverse(x):
    global word_reverse
    for char in x:
        if char not in word_reverse[:0]:
            a = char
            word_reverse = str(a) + str(word_reverse)
        else:
            word_reverse = str(word_reverse)[:1] + str(word_reverse)[0:]
    print(word_reverse)

reverse(input("Anna sõna.\n"))