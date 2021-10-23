# PythonChess
Gioco degli scacchi codificato in Python.

# Come far partire il progetto
Per usare questo programma bisogna avere l'ultima versione di python (3.7+) e semplicemente far partire il main.py presente all'interno del progetto.

# Cosa viene visualizzato
Nella shell di python verranno visualizzati messaggi che guideranno l'utente nella scelta del tipo di modalità richiesta. Dopodiché il sistema creerà diversi output che descrivono lo stato della giocata (disegnandone la scacchiera) e le varie mosse fatte.
Alla fine della giocata il sistema chiederà al giocatore se intende continuare a giocare o meno.

# Tipo di Euristica adottata
L'euristica adottata per questo progetto è abbastanza semplice. Viene dato un valore ad ogni pezzo della scacchiera e la valutazione complessiva di una mossa vede la differenza tra il punteggio del giocatore nero e quello del giocatore bianco. Ogni pedina del giocatore nero incrementa il totale, mentre quelle del giocatore bianco decrementano il totale.
Di seguito riporto la lista dei valori per ogni pezzo:
1. Pedone = 1
2. Cavallo = 3
3. Alfiere = 3 
4. Torre = 5 
5. Donna = 9
6. Re = 500
