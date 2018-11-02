nimi = input("Ütle mulle oma nimi. ")
nimi = str.capitalize(nimi)


omadussõna = input("Ütle mulle üks omadussõna. ")
omadussõna = str.lower(omadussõna)


nimisõna = input("Ütle mulle üks nimisõna. ")
nimisõna = str.lower(nimisõna)


tegusõna = input("Mida sa teed? ")
tegusõna = str.lower(tegusõna)


if not tegusõna.endswith("n"):
    tegusõna = "teen", tegusõna


nimi = str.replace(nimi, 0 and 1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9 and 0, "")


print( "Mina,", nimi + ",", "olen", omadussõna, nimisõna, "ja ma", tegusõna + ".")