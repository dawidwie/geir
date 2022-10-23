

from operator import truediv


sykehjem = {'Kari Nordmann': ['brød', 'egg', 'pølser'], 'Dennis Bojensen': ['gfuel', 'gfuel', 'taco']}


def syk(): 
    print(sykehjem.keys())
    
    navn = str(input("Skriv inn navn av en beboer: "))
    feilmelding = "FINS IKKE"
    for i in sykehjem:
        if navn == i:
            print(f"Denne personen spiser {sykehjem[i][0:3]}")
            feilmelding == False
        else:
            feilmelding == True

    if feilmelding == True:
        print(feilmelding)


syk()