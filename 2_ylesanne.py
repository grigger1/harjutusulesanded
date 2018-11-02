import random

number = int(92 * random.random())
sõnalist = open("sõnad.txt", "r", encoding = "utf8")

sõna = sõnalist.line(number)

print(sõna)