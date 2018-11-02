# tuleb teha poomismäng
import random

number = int(92 * random.random())
sõnalist = open("sõnad.txt", "r", encoding = "utf8")

sõna = sõnalist.readline(number)

print(sõna)