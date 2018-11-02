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


print( "Mina,", nimi + ",", "olen", omadussõna, nimisõna, "ja ma", tegusõna + ".")