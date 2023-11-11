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
    with open("parole_validate_treccani.txt", "w") as valid_file:
        for parola in parole:
            valid_file.write(parola + "\n")



if __name__ == "__main__":
    parole = get_parole()
    parole_treccani = []

    with ThreadPoolExecutor(max_workers=40) as executor:  # Imposta il numero massimo di thread a tuo piacimento
        results = list(tqdm(executor.map(check_parola, parole), total=len(parole)))


    for i, parola in enumerate(parole):
        if results[i]:
            parole_treccani.append(parola)

    scrivi_parole(parole_treccani)

            