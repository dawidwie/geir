# Deloppgave 1

salg = {}
def innlesing(filnavn):
    tekstfil = open(f"{filnavn}", "r")
    tekstfil_alle_verdier = tekstfil.readlines()
    for i in tekstfil_alle_verdier:
        salg[i.split()[0]] = int(i.split()[1])
    return salg

#Deloppgave 2

def maanedensSalgsperson(ordbok):
    mest_salg = 0
    for i in ordbok:
        if ordbok[i] > mest_salg:
            mest_salg = ordbok[i]
            person = i
    print(f"{person} er månedens salgsperson med {mest_salg} salg!")

# Deloppgave 3

def totaltAntallSalg(ordbok):
    samlet_salg = 0
    for i in ordbok:
        samlet_salg += ordbok[i]
    return samlet_salg

# Deloppgave 4

def gjennomsnittSalg(ordbok):
    return totaltAntallSalg(salg) / len(salg)

# Deloppgave 5

def hovedprogram():
    a = innlesing("Applications/Visual Studio Code/grunnleggende/salgstall.txt")
    maanedensSalgsperson(salg)
    print(f"Totalt antall salg: {totaltAntallSalg(salg)}")
    print(f"Gjennomsnittlig antall salg per salgsperson: {gjennomsnittSalg(salg)}")
    print(f"Aktive selgere denne måneden: {len(salg)}")

# Deloppgave 6

hovedprogram()
