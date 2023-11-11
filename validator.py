def get_parole():
    parole = []
    with open("660000_parole_italiane.txt") as file_parole:
        for parola in file_parole:
            parole.append(parola.strip())
    return parole


if __name__ == "__main__":
       print(get_parole()[0]) 