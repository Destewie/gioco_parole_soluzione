FILE_PAROLE = "./parole_validate_treccani.txt"

parole = []
rarezza = {}
n_lettere = 0

if __name__ == "__main__":
    with open(FILE_PAROLE) as f:
        parole = f.readlines()

    parole = [parola.strip() for parola in parole]
    for parola in parole:
        for lettera in parola:
            n_lettere += 1
            if lettera in rarezza:
                rarezza[lettera] += 1
            else:
                rarezza[lettera] = 1
    
    sorted(rarezza)
    tot = 0
    for lettera in rarezza:
        rarezza[lettera] = rarezza[lettera] / n_lettere
        rarezza[lettera] = round(rarezza[lettera], 4)
        rarezza[lettera] = rarezza[lettera] * 100
        tot += rarezza[lettera]
        rarezza[lettera] = str(rarezza[lettera]) + "%"
    
    #sorto la rarezza per la chiave
    rarezza = {k: v for k, v in sorted(rarezza.items(), key=lambda item: item[1])}

    #print each rarezza in a fancy way
    for lettera in rarezza:
        print(lettera, end=" ")
        print(rarezza[lettera])
    print(f"Totale: {tot}", end=" ")


        
