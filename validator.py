import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://www.treccani.it/vocabolario/"

def get_parole():
    parole = []
    with open("660000_parole_italiane.txt") as file_parole:
        for parola in file_parole:
            parole.append(parola.strip())
    return parole

def costruisci_url(parola):
    url = BASE_URL + parola + "/"
    return url

def check_parola(parola):
    url = costruisci_url(parola)
    response = requests.get(url)

    if response.status_code == 200 and url in response.text:
        return True
    elif response.status_code == 200 and url not in response.text:
        return False
    else:
        print("Errore nella richiesta")
        print(f"Status code: {response.status_code}")
        print(f"Url: {url}")
        print(f"Response: {response.text}")
        print("--------------------------------------------------")
        return False


def scrivi_parole(parole):
    with open("parole_validate_treccani.txt", "a") as valid_file:
        for parola in parole:
            valid_file.write(parola + "\n")



if __name__ == "__main__":
    parole = get_parole()
    gruppi_parole = [parole[:100000], parole[100000:200000], parole[200000:300000], parole[300000:400000], parole[400000:500000], parole[500000:600000], parole[600000:]]
    parole_treccani = []

    #voglio parallelizzare il check_parola su oguno dei gruppi di parole

    for i, gruppo in enumerate(gruppi_parole):
        print(f"Gruppo {i}")
        with ThreadPoolExecutor(max_workers=30) as executor:  # Imposta il numero massimo di thread a tuo piacimento
            results = list(tqdm(executor.map(check_parola, gruppo), total=len(gruppo)))

        parole_verificate_per_gruppo = 0
        for i, parola in enumerate(gruppo):
            if results[i]:
                parole_verificate_per_gruppo += 1
                parole_treccani.append(parola)

        scrivi_parole(parole_treccani)

        #un po' di stats
        print(f"Parole totali: {len(gruppo)}")
        print(f"Parole presenti anche sulla Treccani: {parole_verificate_per_gruppo}")
        print("--------------------------------------------------")
        