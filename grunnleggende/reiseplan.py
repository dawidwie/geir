''

reiseomrade = []
klesplagg = []
avreisedato = []
reiseplan = []
for i in range(5):

    omrade = str(input(("Skriv inn et reiseområde:")))
    reiseomrade.append(omrade)



for i in range(5):

    plagg = str(input(("Skriv inn et klesplagg:")))
    klesplagg.append(plagg)



for i in range(5):

    dato = str(input(("Skriv inn en avreisedato:")))
    avreisedato.append(dato)


reiseplan.append(reiseomrade)
reiseplan.append(klesplagg)
reiseplan.append(avreisedato)

for i in range(len(reiseplan)):
    print(reiseplan[i])

i1 = int(input("Skriv inn 0 for reiseomrade, 1 for klesplagg og 2 for avreisedato: "))
i2 = int(input("Skriv inn mellom 1-5 for hvilket element du vil se: "))

if i1 == 0 or i1 == 1 or i1 == 2:
    if i2-1 == 0 or 1 or 2 or 3 or 4:
        print(reiseplan[i1][i2])
else:
    print("vi finner dette inte i database")
