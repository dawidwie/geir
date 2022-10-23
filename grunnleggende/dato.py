

def dato():
    dag = int(input("Skriv inn en dag som tall: "))
    maned = int(input("Skriv inn en måned som tall: "))
    print(dag, ",", maned)
    dag2 = int(input("Skriv inn en dag som tall: "))
    maned2 = int(input("Skriv inn en måned som tall: "))
    print(dag2,",",maned2)

    print(type(maned))

    if maned > maned2:
        print("Riktig rekkefolge")
    elif maned2 > maned:
        print("Feil rekkefolge")
    elif maned == maned2:
        if dag > dag2:
            print("Riktig rekkefolge")
        elif dag2 < dag:
            print("Feil rekkefolge")
        if dag == dag2:
            print("Samme dato!")
    else:
        print("hva")

dato()