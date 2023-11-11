if __name__ == "__main__":
    parole_tutte = []
    parole_lunghe = []


    with open("parole_validate_treccani.txt", "r") as file_parole_validate:
        for parola in file_parole_validate:
            parole_tutte.append(parola.strip())
    
    parole_tutte.sort()
            
    for i, parola in enumerate(parole_tutte):
        if(i < len(parole_tutte)-1):
            if(parole_tutte[i] not in parole_tutte[i+1]):
                parole_lunghe.append(parola)
    parole_lunghe.append(parole_tutte[-1])
    
    with open("parole_lunghe_treccani.txt", "w") as file_parole_lunghe:
        for parola in parole_lunghe:
            file_parole_lunghe.write(parola + "\n")

