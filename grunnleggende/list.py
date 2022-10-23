

def opp7():

    liste = [2, 3, 5]

    nytall = int(input("Skriv inn et tall: "))

    liste.append(nytall)

    print(liste[0], liste[2])

    addisjon = sum(liste)

    resultat = 1
    for x in liste:
        resultat = resultat * x


    matteliste = [resultat, addisjon]

    fullListe = [liste, resultat, addisjon]

    print(fullListe)

    navnliste = []

    navn1 = input("Skriv inn et navn: ")
    navn2 = input("Skriv inn et navn: ")
    navn3 = input("Skriv inn et navn: ")
    navn4 = input("Skriv inn et navn: ")

    navnliste.append(navn1)
    navnliste.append(navn2)
    navnliste.append(navn3)
    navnliste.append(navn4)

    if "dawid" in navnliste:
        print("Du husket meg!")
    else:
        print("Glemte du meg?")

    print(navnliste)







opp7()

