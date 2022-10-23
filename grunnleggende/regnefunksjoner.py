

def addisjon(tall1, tall2):
    summ = tall1 + tall2
    print(f"Summ under addisjon er {summ}")


def subtraksjon(tall1, tall2):
    summ = tall1 - tall2
    print(f"Summ under subtraksjon er {summ}")

def divisjon(tall1, tall2):
    summ = tall1 / tall2
    print(f"Summ under divisjon er {summ}")

def tommerTilCm(antallTommer):
    summ = antallTommer*2.54
    print(f"{antallTommer} tommer blir til {summ} cm")


def skrivBeregninger():
    t1 = int(input("Skriv inn et tall: "))
    t2 = int(input("Skriv inn et til tall: "))

    addisjon(t1,t2)
    subtraksjon(t1,t2)
    divisjon(t1,t2)

    tommer = int(input("Skriv inn et tall som blir regnet som tommer: "))
    tommerTilCm(tommer)

skrivBeregninger()

