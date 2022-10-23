

salg = {}
def innlesing(filnavn):
    tekst = open(f"{filnavn}", "r")
    tekstAlt = tekst.readlines()
    for i in tekstAlt:
        salg[i.split()[0]] = int(i.split()[1])
    return salg

def maanedensSalgsperson(ordbok):
    mestSalg = 0
    for i in ordbok:
        if ordbok[i] > mestSalg:
            mestSalg = ordbok[i]
            person = i
    print(f"{person} er maanedens salgsperson med {mestSalg} salg")

def totaltAntallSalg(ordbok):
    antallSalg = 0
    for i in ordbok:
        antallSalg += ordbok[i]
    
    return antallSalg

def gjennomsnittSalg(ordbok):
    antallSalg = 0
    antall = 0
    for i in ordbok:
        antallSalg += ordbok[i]
        antall += 1
    
    gjennomsnitt = antallSalg/antall
    return gjennomsnitt

def hovedprogram():
    a = innlesing('/Applications/VisualStudioCode/grunnleggende/salgstall.txt')
    maanedensSalgsperson(salg)
    print(f"Aktive selgere denne maaneden: {len(salg)}")
    print(f"Gjennomsnittlig salg per person: {gjennomsnittSalg(salg)}")
    print(f"Totalt antall solgt: {totaltAntallSalg(salg)}")

hovedprogram()