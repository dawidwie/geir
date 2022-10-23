

talliste = []

def adder(tall1, tall2):
    global talliste
    resultat = tall1+tall2

    talliste.append(f"Resultatet er: {resultat}")

adder(4,7)
adder(4,8)

print(talliste)

def bokstaver():
    antall = 0
    streng = str(input("Skriv inn en tekststreng: "))
    bokstav = str(input("Skriv inn en bokstav du vil lete etter i tekststrengen: "))

    for i in streng:
        if bokstav == i:
            antall += 1
    
    print(f"Det er {antall} {bokstav} i strengen")

bokstaver()

streng = str(input("Skriv inn en tekststreng: "))
bokstav = str(input("Skriv inn en bokstav du vil lete etter i tekststrengen: "))

def tellForekomst(minTekst, minBokstav):
    antall = 0

    for i in minTekst:
        if minBokstav == i:
            antall += 1
    
    print(f"Det er {antall} {bokstav} i strengen")


tellForekomst(streng, bokstav)