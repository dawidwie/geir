

Dict = {'melk': 14.90, 'brød': 24.90, 'yoghurt': 12.90, 'pizza': 39.90}
print(Dict)

ny = []

vare1 = str(input("Skriv inn navn på vare: "))
pris1 = int(input("Skriv inn pris på vare: "))
vare2 = str(input("Skriv inn navn på annen vare: "))
pris2 = int(input("Skriv inn pris på den andre varen: "))

Dict[vare1] = pris1
Dict[vare2] = pris2
print(Dict)