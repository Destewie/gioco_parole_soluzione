# Gioco delle parole
TODO: Scrivere le regole

# Analisi sulle parole della lingua italiana 
Voglio riuscire a fare analisi dati sull'insieme di parole che non sono radice di nessun'altra parola 

# Come farlo 
Non ho trovato dataset ufficiali Treccani (potevo immaginarlo).


L'unica è confrontare il dataset delle 660000 parole italiane per vedere quali effettivamente ci sono sulla treccani.


Per fare questo, faccio richieste a _https://www.treccani.it/vocabolario/parola/_ 

# Cosa fare con i dati ottenuti
Un engine per il gioco delle lettere.


Input:
* Numero di giocatori
* Posto all'interno del giro
* Lettere dette prima di te

Output:
Best move a livello probabilistico


 
_Piccolo disclaimer: Alla fine del processo descritto sopra, non avrò in mano l'intero dataset delle parole italiane Treccani, ma ce lo facciamo andare bene comunque_ 

