import anytree

if __name__ == "__main__":
    with open('660000_parole_italiane.txt', 'r') as dizionario:
        parole = dizionario.read().splitlines()
        for i in range(1, 10):
            print(parole[i])
        

