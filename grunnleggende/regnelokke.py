

def tall():
    x = int
    liste =[]
    minsum = 0
    while x != 0:
        tallet = int(input("Skriv inn et tall: "))
        x = tallet
        liste.append(x)
        minsum += x
    minste = liste[0]
    storste = liste [0]
    for i in range(len(liste)):
        print(liste[i])
        
    for i in range(len(liste)):
        if liste[i] < minste:
            minste = liste[i]


    for i in range(len(liste)):
        if liste[i] > storste:
            storste = liste[i]

    print(f"Summen av dine svar ble {minsum}")
    print(f"Det minste tallet du skrev inn var {minste}, og det største var {storste}")

tall()