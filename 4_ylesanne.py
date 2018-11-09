from collections import Counter

sõnad = [(input("Kopeeri tekst."))]

sõnad = sõnad.sort

while not sõnad == []:

    word = sõnad [0]
    print(word, ":", Counter.values(word in sõnad) + "\n")
    sõnad.remove()[0:]