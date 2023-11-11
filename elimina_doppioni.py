if __name__ == "__main__":
    parole = []
    with open("parole_validate_treccani.txt", "r") as file_parole:
        for parola in file_parole:
            parole.append(parola.strip())

    parole = set(parole)

    with open("parole_validate_treccani.txt", "w") as file_parole:
        for parola in parole:
            file_parole.write(parola + "\n")
