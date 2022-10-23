

mineOrd = []

def slaasammen(str1,str2):
    global mineOrd
    sammen = str1 + str2
    print(sammen)
    mineOrd.append(sammen)




def skrivUt(liste):
    for i in range(len(liste)):
        print(liste[i])



tekst = ' ' 

while tekst:
    inpp = str(input("Skriv inn 'i' for slå sammen, 'u' for skrivUt og 's' for å gå ut av programmet: "))
    if inpp == 'i':
        s1 = input("Skriv inn en streng: ")
        s2 = input("Skriv inn en til streng: ")
        slaasammen(s1,s2)
    elif inpp == 'u':
        skrivUt(mineOrd)
    elif inpp == 's':
        print("hade")
        break
    else: 
        print("Ikke en akseptert verdi")
            
        



