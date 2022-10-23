

def bilett():
    alder = int(input("Skriv inn din alder: "))
    navn = str(input("Skriv inn ditt navn: "))

    bilettpris = 0
    if alder <= 17: 
        bilettpris += 30
    elif alder >=  18 and alder <= 62:
        bilettpris += 50    
    else:
        bilettpris += 35

    print(f"Hei {navn}, din bilett vil koste {bilettpris}kr")

bilett()