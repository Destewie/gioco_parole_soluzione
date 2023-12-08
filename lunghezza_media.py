FILE_SENZA_RADICI = "parole_lunghe_treccani.txt"

def get_parole(file_name):
    parole = []
    with open(file_name) as file_parole:
        for parola in file_parole:
            parole.append(parola.strip())
    return parole

if __name__ == "__main__":
    parole = []
    somma_lunghezze = 0
    with open(FILE_SENZA_RADICI) as file_parole:
        for parola in file_parole:
            somma_lunghezze += len(parola.strip())
            parole.append(parola.strip())
    
    print(f"Lunghezza media di una parola per il gioco delle lettere: {somma_lunghezze/len(parole)}")
    