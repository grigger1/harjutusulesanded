# tuleb teha poomismäng
import random

elud = 3

pakutud = []
pakutud_print = ""

number = round(92 * random.random())
sõnalist = open("sõnad.txt", "r", encoding = "utf8")

sõna = sõnalist.readline(number)

with sõnalist as list1:
    for i, line in enumerate(list1):
        if i == number:
            sõna = sõnalist.readline()[:-1]

print (len(sõna) * "_" + "\nVastus on", len(sõna), "tähte pikk. \n\n")

while elud > 0:
    täht = input("Arva, mis täht võiks sõnas olla.\n")
    vastus_näit = ""
    pakutud += täht
    olemas = 0

    pakutud_print = pakutud_print + täht
    print("\npakutud:", sorted(pakutud_print))

    for char in sõna:
        if char in pakutud:
            vastus_näit += char
            if täht in sõna:
                olemas += 1
        else:
            vastus_näit += "_"

    print("\n" + vastus_näit + "\n")

    if vastus_näit == sõna:
        print("Sa võitsid.")
        break

    if olemas == 0:
        elud -= 1
        if elud == 0:
            print("Sa kaotasid. \nÕige vastus oli", sõna +".")
            break
        else:
            if elud - 1 == 1:
                print("Seda tähte sõnas ei ole. \nSa saad 1 korra veel valesti panna.")
            else:
                print("Seda tähte sõnas ei ole. \nSa saad", elud - 1, "korda veel valesti panna.")

print("Mäng sai läbi.")