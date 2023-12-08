FILE_PAROLE = "./parole_validate_treccani.txt"

if __name__ == "__main__":
    # in realtà voglio le parole che, scegliendo la seconda lettera, portano solo a parole di lunghezza 3
    with open(FILE_PAROLE) as f:
        parole = f.readlines()
        parole = [parola.strip() for parola in parole]

        min_len = 9999999
        parola_corta = ""

        for i, parola in enumerate(parole):
            if (i == len(parole)-1):
                print(parola)
            elif len(parola) == 3 and not (parola in parole[i+1]):
                print(parola)
