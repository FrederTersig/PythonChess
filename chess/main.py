#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import GameModels as G
import Heuristics as H
import copy
from GameModels import chessState

heuristic = H.ChessHeuristic()
game = G.ChessGame(heuristic)
print('INIZIO DEL PROGRAMMA')


#1) Ciclo per fare più partite.
#2) Ciclo per giocatore vs pc O pc vs pc
#3) Conteggio delle partite fatte, vittorie & aumento del punteggio dell'euristica usata.

choosePC = False # Booleana per la scelta della modalità (Human vs Pc || Pc vs Pc)

while True:
	print('####################')
	print('** Digita "PC" per far giocare il computer contro se stesso. **')
	print('** Digita "Human" per giocare contro il computer. **')
	print('####################')
	chooseA = input()
	print(type(chooseA))
	if type(chooseA) is not str:
		print('digita di nuovo quale modalità vuoi provare')
		continue
	elif type(chooseA) is str and chooseA == 'PC':
		print('Il PC giocherà contro se stesso')
		choosePC = True
		break
	elif type(chooseA) is str and chooseA == 'Human':
		print('Il PC giocherà contro di te')
		choosePC = False
		break
	print('####################')

if not choosePC:
# ----------------------------------------------- While per la scelta della giocata Human vs Pc
	while True:
		
		try:
			print('#################################')
			print('Quale strategia di scelta per il PC? [Scrivi il numero corrispondente]:')
			print('(1) per Minimax; (2) per AlfaBeta Pruning; (3) per Negamax')
			print('### Scrivi il numero della strategia scelta, la virgola e infine la profondità desiderata ###')
			print('### Per esempio: 1,5 è algoritmo Minimax con profondità 5 ###')
			print('*** NOTA: Usando profondità maggiore a 3 si allungherà di molto il tempo di decisione***')
			print('#################################')
			chooseInput = tuple(map(int,input().split(',')))
			if type(chooseInput) is not tuple:
				print('Inserisci correttamente i due numeri separati dalla virgola. riprova')
				continue
			elif type(chooseInput[0]) is not int or type(chooseInput[1]) is not int:
				print('Bisogna inserire due numeri. riprova.')
				continue
			elif chooseInput[0] > 3 or chooseInput[0] <= 0:
				print('Il primo numero deve essere uguale ad 1, 2 o 3.') 
				continue
		except ValueError:
			print('Errore: Bisogna digitare un valore corretto. riprova.')
			continue
		#print('sei riuscito- Algoritmo', chooseInput[0], '| Profondità ', chooseInput[1])
		euristicaPC = chooseInput[0]
		livello = chooseInput[1]
		break

	# ---------------------------------------------------------- > Procede con il gioco

	if euristicaPC == 1:
		print('@@@ Hai scelto la strategia Minimax con profondità = ', livello)
	elif euristicaPC == 2:
		print('@@@ Hai scelto la strategia AlfaBeta con profondità = ', livello)
	else:
		print('@@@ Hai scelto la strategia Negamax con profondità = ', livello)



	print('MOSTRO LO STATO BASE')
	stato = game.getState()
	giocata = []
	game.checkState(stato.getBoard())
	game.checkPieces(stato.getWhitePieces(), stato.getBlackPieces())
	game.checkPieces(stato.getWhiteDict(), stato.getBlackDict())
	print('------ INIZIA IL GIOCO! -------')

	while True:
		turn = 'w' # Turno del giocatore

		choosing = False
		xState = None # Mi serve per checkare lo stato!
		
		while not choosing:        
			
			print('PROVA INIZIALE: --> Per inserire i due numeri bisogna che questi siano divisi da una virgola = x, y')
			try:
				
				pezzoScelto = tuple(map(int,input().split(',')))
				#Se il pezzo non fa parte del dizionario dei bianchi, bisogna re inserire le coordinate
				if pezzoScelto not in stato.getWhiteDict():
					print('Non è presente nessun pezzo bianco in queste coordinate: Bisogna reinserire coordinate del pezzo scelto')
					continue
				elif type(pezzoScelto) is not tuple:
					print('Inserisci correttamente le coordinate del pezzo scelto => x,y')
					continue
				elif type(pezzoScelto[0]) is not int or type(pezzoScelto[1]) is not int:
					print('Inserisci correttamente le coordinate usando soltanto numeri! => x,y')
					continue
			except ValueError:
				print('Errore: Reinserire Input del pezzo scelto')
				continue
			
			pezzo = stato.getWhiteDict()[pezzoScelto]
			#Per avere il 'dettaglio' delle lettere del pezzo, bisogna usare stato.getPiece(pezzoScelto[0],pezzoScelto[1])
			listaMosse = stato.pieceMovement(pezzoScelto[0], pezzoScelto[1], pezzo, turn)  # C'è un problema con pieceMovement
			if not listaMosse:  # il pezzo scelto non p
				print('Il pezzo scelto non può fare mosse : Scegliere un altro pezzo') # Il problema è sullo spostamento del re quando è sotto minaccia
				continue
			
			print('::Elenco di mosse possibili per il pezzo scelto::')      
			for m in listaMosse:
				print('[[ ', pezzoScelto , ' => ', m ,']]')
					 
			
			#game.checkState(stato.representation.board)       
			print('Inserisci le coordinate in cui si desidera spostare il pezzo scelto')
			inserimento = False
			while not inserimento:
				try:
					spostamentoScelto = tuple(map(int,input().split(',')))
					if spostamentoScelto not in listaMosse:
						print ('La destinazione non è corretta, reinserisci una destinazione ')
						choosing = False
						continue
					elif type(spostamentoScelto) is not tuple:
						print('Errore: Le coordinate dello spostamento sono state inserite in maniera erronea. Rispettare sempre il formato x,y') # Reinserire spostamento
						continue
					elif type(spostamentoScelto[0]) is not int or type(spostamentoScelto[1]) is not int:
						print('Errore: Le coordinate dello spostamento sono incorrette, assicurarsi di scrivere i numeri delle coordinate rispettando il formato x,y') # reinserire spostamento
						continue
					inserimento = True
				except ValueError:
					print('Errore: Reinserire Input dello spostamento scelto')
					continue
			
			# Vado a mettere i valori degli input in delle variabili più facili da manipolare
			x = pezzoScelto[0]
			y = pezzoScelto[1]
			xe = spostamentoScelto[0]
			ye = spostamentoScelto[1]

			choosing = True
			if stato.isFree(xe, ye):
				# 1° -> En Passant
				#print('stato obiettivo isFREE --> en passant? [TUTTE TRUE]')
				print(stato.checkEP(x,ye), ' - ', turn, ' - ', stato.checkPiece(x,y,'p'))
				if stato.checkPiece(x,y,'p') and turn == 'w' and (ye-y == 1 or ye-y== -1) and stato.checkEP(x, ye): # SBAGLIO IN CHECKEP
					#print('IL GIOCATORE BIANCO TENTA EN PASSANT')
			
					wnumber = stato.getWhitePieces()
					bnumber = stato.getBlackPieces()
					bnumber = game.reducePieces('p',bnumber) # Rimosso il mangiato per en-passant
					bpos = stato.getBlackDict()
					wpos = stato.getWhiteDict()

					ped = wpos[x,y]
					del wpos[x,y]
					wpos[xe,ye] = ped
					del bpos[x,ye]
					gridB = stato.getBoard()
					gridB[x,ye] = '0'
					ped = gridB[x,y]
					gridB[x,y] = '0'
					gridB[xe,ye] = ped
						
					xState = chessState(stato.H, gridB, wnumber, bnumber,wpos,bpos)

				else:              
					xState = game.moving(stato, x, y, xe, ye,turn)
					#2° -> Upgrade del Pedone Bianco che arriva in fondo alla griglia
					if xState.checkPiece(xe,ye,'p') and xe == 0 and turn == 'w': # w è il giocatore
						# Puoi promuovere il pedone --> upgradePlayerPawn
						bPieces = xState.getBlackPieces()
						wPieces = xState.getWhitePieces()
						board = xState.getBoard()
						bDict = xState.getBlackDict()
						wDict = xState.getWhiteDict()
		
						scelta = game.upgradePlayerPawn()
		
						oldPiece = board[xe,ye]
						newPiece = scelta + oldPiece[1] + oldPiece[2]
						board = game.setPiece(xe,ye,newPiece,board)
						wPieces = game.reducePieces('p',wPieces)
						#wPieces = game.reducePieces(scelta,wPieces) # QUI VA AGGIUNTO 1 PEZZO NON RIMOSSO
						wPieces = game.addPieces(scelta,wPieces)
		
						del wDict[xe,ye]
						wDict[xe,ye] = scelta
		
						xState = chessState(stato.H, board, wPieces, bPieces, wDict, bDict)
						del bPieces,wPieces,board,bDict,wDict,scelta,oldPiece,newPiece
						
			else:
				if stato.getPieceTurn(xe,ye) == turn and x == xe:
					diz = stato.getWhiteDict()
					if (diz[xe,ye] == 'r' and diz[x,y]=='t') or (diz[xe,ye] == 't' and diz[x,y]=='r'):
						# Da modificare --
						#Si parte da una T e l'arrivo è nella casella del re
						brd = copy.deepcopy(stato.getBoard())
									
						if abs(y-ye) == 4:
							if diz[x,y] =='r':
								diz = game.doCastlingSwitch(diz, x, y, x, y-2)
								brd = game.doCastlingSwitch(brd,x,y,x,y-2)
								stringaA = brd[x,y-2][0] + brd[x,y-2][1] + 's' 
								brd[x,y-2]=stringaA
								# Torre di 3
								diz = game.doCastlingSwitch(diz,xe,ye,xe,ye+3)
								brd = game.doCastlingSwitch(brd,xe,ye,xe,ye+3)
								stringaB = brd[xe,ye+3][0] + brd[xe,ye+3][1] + 's' 
								brd[xe,ye+3]=stringaB
							else:
								# Torre di 3
								diz = game.doCastlingSwitch(diz, x, y, x, y+3)
								brd = game.doCastlingSwitch(brd,x,y,x,y+3)
								stringaA = brd[x,y+3][0] + brd[x,y+3][1] + 's' 
								brd[x,y+3]=stringaA
								# Re di 2
								diz = game.doCastlingSwitch(diz,xe,ye,xe,ye-2)
								brd = game.doCastlingSwitch(brd,xe,ye,xe,ye-2)
								stringaB = brd[xe,ye-2][0] + brd[xe,ye-2][1] + 's' 
								brd[xe,ye-2]=stringaB
											
						elif abs(y-ye) == 3:
							if diz[x,y] =='r': # QUI C'E' L'ERRORE
								#Torre a y-2
								diz = game.doCastlingSwitch(diz, x, y, x, y+2)
								brd = game.doCastlingSwitch(brd,x,y,x,y+2)
								stringaA = brd[x,y+2][0] + brd[x,y+2][1] + 's' 
								brd[x,y+2]=stringaA
								#Re a y+2   # --- > CREO MOLTEPLICI COPIE DEI DIZIONARI :: SOLUZIONE PER FARLO SOLO UNA VOLTA?
								diz = game.doCastlingSwitch(diz,xe,ye,xe,ye-2)
								brd = game.doCastlingSwitch(brd,xe,ye,xe,ye-2)
								stringaB = brd[xe,ye-2][0] + brd[xe,ye-2][1] + 's' 
								brd[xe,ye-2]=stringaB
							else:
								#Torre a y-2
								diz = game.doCastlingSwitch(diz, x, y, x, y-2)
								brd = game.doCastlingSwitch(brd,x,y,x,y-2)
								stringaA = brd[x,y-2][0] + brd[x,y-2][1] + 's' 
								brd[x,y-2]=stringaA
								#Re a y+2   # --- > CREO MOLTEPLICI COPIE DEI DIZIONARI :: SOLUZIONE PER FARLO SOLO UNA VOLTA?
								diz = game.doCastlingSwitch(diz,xe,ye,xe,ye+2)
								brd = game.doCastlingSwitch(brd,xe,ye,xe,ye+2)
								stringaB = brd[xe,ye+2][0] + brd[xe,ye+2][1] + 's' 
								brd[xe,ye+2]=stringaB
						else:
							print('ERRORE: NEIGHBORS ARROCCO SBAGLIATO!')

						# Quindi abbiamo brd = griglia, diz = dizionario BLACK --
						diz_b = stato.getBlackDict()
									
						wPies = stato.getWhitePieces() # Dizionario dei pezzi
						bPies = stato.getBlackPieces()
									
						xState = chessState(stato.H, brd,wPies,bPies,diz,diz_b)
						#del wPies,bPies,stringaA,stringaB,diz,brd
					else:
						print('ERRORE CON ARROCCO MAIN --> RE / TORRE NO; TORRE / RE NO')
				else:
					xState = game.doEat(stato, x, y, xe, ye, turn)
					#2° -> Promozione del pedone : In questo caso ci arriva mangiando una pedina avversaria
					if xState.checkPiece(xe,ye,'p') and xe == 0 and turn == 'w': # w è il giocatore
						# Puoi promuovere il pedone --> upgradePlayerPawn
						bPieces = xState.getBlackPieces()
						wPieces = xState.getWhitePieces()
						board = xState.getBoard()
						bDict = xState.getBlackDict()
						wDict = xState.getWhiteDict()
		
						scelta = game.upgradePlayerPawn()
		
						oldPiece = board[xe,ye]
						newPiece = scelta + oldPiece[1] + oldPiece[2]
						board = game.setPiece(xe,ye,newPiece,board)
						wPieces = game.reducePieces('p',wPieces)
						wPieces = game.addPieces(scelta,wPieces)
		
						del wDict[xe,ye]
						wDict[xe,ye] = scelta
		
						xState = chessState(stato.H, board, wPieces, bPieces, wDict, bDict)
						del bPieces,wPieces,board,bDict,wDict,scelta,oldPiece,newPiece
					
						
			#SE lo stato di arrivo è una pedina, si mangia, altrimenti non si mangia! (doEat, moving)
			#Ricorda che ti manca l'upgrade del PEDONE quando arriva all'ultima casella !!!!!!!
			#Alla fine del while, prima di chiuderlo, controllo che questa sia una mossa ottimale e che non metta a rischio    
			#Il re. Quindi se va bene procedo nel registrare la mossa altrimenti il giocatore dovrà inserire di nuovo una
			#mossa lecita.
			if game.checkKing(xState, xState.getWhiteDict(), 'w'):
				#print('IL RE NON HA PERICOLI')
				stato = copy.deepcopy(xState)
				game.checkState(stato.getBoard())
				giocata.append(stato)

				if game.checkWin(stato, stato.getBlackDict()):
					print('################## I BIANCHI VINCONO!! ###################')
					break

			else:
				print('La mossa lascia scoperto il proprio RE!! Inserire una nuova mossa!')
				choosing = False
				continue

		########################
		# Turno del pc : NERO
		turn = 'b'
		mx = -9999
		states = game.neighbors(turn, stato)

		if len(states) > 0:
			#print('Comincia il for degli stati nel main')
			if euristicaPC == 1: # H1
				for s in states: 
					#h = heuristic.H3(game,s,livello,-1000,+1000,turn)
					#h = heuristic.H2(game,s,3,-1000,+1000,turn)
					h = heuristic.H1(game,s,livello,turn)  # Funzione che pesa di più
					#print('valore euristica: ', h)
					if h is None:
						print(h)
						print(' h è none')
						game.checkState(s.getBoard())
					if h>mx:
						mx = h
						stato = s
			elif euristicaPC == 2: #H2
				for s in states:
					#h = heuristic.H3(game,s,livello,-1000,+1000,turn)
					h = heuristic.H2(game,s,livello,-1000,+1000,turn)
					#h = heuristic.H1(game,s,livello,turn)  # Funzione che pesa di più
					#print('valore euristica: ', h)
					if h is None:
						print(h)
						print(' h è none')
						game.checkState(s.getBoard())
					if h>mx:
						mx = h
						stato = s
			else: #H3
				for s in states:
					h = heuristic.H3(game,s,livello,-1000,+1000,turn)
					#h = heuristic.H2(game,s,3,-1000,+1000,turn)
					#h = heuristic.H1(game,s,livello,turn)  # Funzione che pesa di più
					#print('valore euristica: ', h)
					if h is None:
						print(h)
						print(' h è none')
						game.checkState(s.getBoard())
					if h>mx:
						mx = h
						stato = s
			giocata.append(stato)
			# !!!! DEVO CHECKARE ANCHE LO STATO DEL BLACK PERCHE SE NON PUO' MUOVERE PIU' IL RE LA PARTITA FINISCE!!!!    
			if game.checkWin(stato,stato.getWhiteDict()): # Vittoria?
				print('################### I NERI VINCONO!!!! ###########################')
				#game.checkState(stato.getBoard())
				break
			else:
				print('#################### MOSSA DEI NERI###########################')
				game.checkState(stato.getBoard())
				#game.checkPieces(stato.getWhitePieces(), stato.getBlackPieces())
				#game.checkPieces(stato.getWhiteDict(), stato.getBlackDict())
				print('##################################################################')
				# stato --> è quello scelto dal computer : manca solo la condizione di vittoria
		else:
			print('###  SCACCO MATTO DEI BIANCHI : I NERI HANNO PERSO! ###')
			game.checkState(stato.getBoard())
			break

	print('FINE PARTITA!')
	for n,x in enumerate(giocata):
		print('----------- > ', n+1, ' ° mossa')
		game.checkState(x.getBoard())
		print('-----------------------------')
else:
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#Questa è la parte in cui il PC gioca contro il PC, facciamo prima un test per vedere se ci si arriva.
#----------------------------------------------------------------------- PC VS PC
	#Prima di tutto, variabili per la parte adaptive:
	matchCount = 1 # Variabile che serve per contare le partite fatte
	hPoint = [0,0,0] # array che contiene i punteggi presi da ogni euristica
	win = [0,0,0]
	lost = [0,0,0]
	draw = [0,0,0]
	hScelta = 0
	hPointB = [0,0,0]
	hSceltaB = 0
	#Esiti è un vettore che tiene conto delle vittorie di una specifica euristica contro un'altra specifica euristica
	
	stat =[]



	result = ''
	#dovrebbero bastare
	conteggioPatta = 0
	
	

	while True: # CICLO DI RIPETIZIONE
		# STATO INIZIALE---->
		conteggioPatta=0
		stato = game.getState()
		giocata = []
		game.checkState(stato.getBoard())
		game.checkPieces(stato.getWhitePieces(), stato.getBlackPieces())
		game.checkPieces(stato.getWhiteDict(), stato.getBlackDict())
		numTurno = 0

		# Parte in cui si sceglie quale euristica usare
		if hPoint[0] >= hPoint[1] and hPoint[0] >= hPoint[2]:
			# La prima euristica è la migliore
			hScelta = 0
		elif hPoint[1] >= hPoint[0] and hPoint[1] >= hPoint[2]:
			# La seconda euristica è la migliore
			hScelta = 1
		
		elif hPoint[2] >= hPoint[0] and hPoint[2] >= hPoint[1]:
			# La terza è la migliore ed è la PRIMA ad essere usata.
			hScelta = 2
		

		# Parte in cui si sceglie quale euristica usare
		if hPointB[0] >= hPointB[1] and hPointB[0] >= hPointB[2]:
			# La prima euristica è la migliore
			hSceltaB = 0
		elif hPointB[1] >= hPointB[0] and hPointB[1] >= hPointB[2]:
			# La seconda euristica è la migliore
			hSceltaB = 1
		
		elif hPointB[2] >= hPointB[0] and hPointB[2] >= hPointB[1]:
			# La terza è la migliore ed è la PRIMA ad essere usata.
			hSceltaB = 2

		print('------>>>>>>>> Inizia di nuovo! Partita numero :', matchCount)


		###############################################################################################################
		while True: # CICLO DI GIOCO
			#Turno del pc : BIANCO
			print('-- Turno dei BIANCHI')
			turn = 'w' # Turno del giocatore
			vecchioBD = len(stato.getBlackDict())

			mn = 9999
			states = game.neighbors(turn,stato)
			#I bianchi usano un'euristica semplicissima, soltanto per vedere come va
			if len(states) > 0:
				for s in states:

					#h = heuristic.H1(game,s,0,turn)
					if hScelta == 0:
						h = heuristic.H1(game,s,1,turn)
					if hScelta == 1:
						h = heuristic.H2(game,s,1,-1000,+1000,turn)
					else:
						h = heuristic.H3(game,s,1,-1000,+1000,turn)

					if h is None:
						print('--- Errore, check della Board. Turno > ', turn)
						game.checkState(s.getBoard())
					if h<mn:
						mn = h
						stato = s
				numTurno = numTurno + 1
				giocata.append(stato)

				if game.checkWin(stato,stato.getBlackDict()): # Vittoria?
					print('################### I BIANCHI VINCONO!!!! ###########################')
					#game.checkState(stato.getBoard())
					result = 'w'
					break
				else:
					if game.checkDraw(stato):
						print('PATTA-----! RE vs RE ; RE vs ALF/RE ; RE VS CAV/RE')
						#game.checkState(stato.getBoard())
						result = 'x'
						break

					if len(stato.getBlackDict()) == vecchioBD:
						#NOn ho mangiato, comincio il conteggio per la patta:
						conteggioPatta = conteggioPatta + 1
					
					if conteggioPatta >= 100:
						print('PATTA! 100 mosse senza mangiare nulla')
						game.checkState(stato.getBoard())
						result = 'x'
						break
					
					#print('#################### MOSSA DEI BIANCHI###########################')
					#game.checkState(stato.getBoard())
					#game.checkPieces(stato.getWhitePieces(), stato.getBlackPieces())
					#game.checkPieces(stato.getWhiteDict(), stato.getBlackDict())
					#print('##################################################################')
					# stato --> è quello scelto dal computer : manca solo la condizione di vittoria
					
			else:
				print('###  SCACCO MATTO DEI NERI : I BIANCHI HANNO PERSO! ###')
				game.checkState(stato.getBoard())
				result = 'l'
				break
			#------------------------------------------------------------------------
			# Turno del pc : NERO
			print('-- Turno dei NERI')
			turn = 'b'
			vecchioWD = len(stato.getWhiteDict())
			mx = -9999
			states = game.neighbors(turn, stato)

			if len(states) > 0:
				#print('Comincia il for degli stati nel main')
				for s in states:
					if hSceltaB == 0:
						h = heuristic.H1(game,s,0,turn)
					if hSceltaB == 1:
						h = heuristic.H2(game,s,1,-1000,+1000,turn)
					else:
						h = heuristic.H3(game,s,1,-1000,+1000,turn)

					if h is None:
						print('---- ERRORE , h è none! TURNO: ', turn)
						game.checkState(s.getBoard())
					if h>mx:
						mx = h
						stato = s
				numTurno = numTurno + 1
				giocata.append(stato)
				
				if game.checkWin(stato,stato.getWhiteDict()): # Vittoria?
					print('################### I NERI VINCONO!!!! ###########################')
					#game.checkState(stato.getBoard())
					result = 'l'
					break
				else:
					if game.checkDraw(stato):
						print('PATTA-----! RE vs RE ; RE vs ALF/RE ; RE VS CAV/RE')
						game.checkState(stato.getBoard())
						result = 'x'
						break

					if len(stato.getWhiteDict()) == vecchioWD:
						#NOn ho mangiato, comincio il conteggio per la patta:
						conteggioPatta = conteggioPatta + 1
					
					if conteggioPatta >= 100:
						print('PATTA! 100 mosse senza mangiare nulla')
						game.checkState(stato.getBoard())
						result = 'x'
						break
					#print('#################### MOSSA DEI NERI###########################')
					#game.checkState(stato.getBoard())
					#game.checkPieces(stato.getWhitePieces(), stato.getBlackPieces())
					#game.checkPieces(stato.getWhiteDict(), stato.getBlackDict())
					#print('##################################################################')
					# stato --> è quello scelto dal computer : manca solo la condizione di vittoria
					
			else:
				print('###  SCACCO MATTO DEI BIANCHI : I NERI HANNO PERSO! ###')
				#game.checkState(stato.getBoard())
				result ='w'
				break
		########################################################################################################################
		
		print('- Numero di mosse totale di questa partita: ', numTurno)
		print(' - MOSTRO STATI -')
		for n,x in enumerate(giocata):
			print('----------- > ', n+1, ' ° mossa')
			game.checkState(x.getBoard())
			print('-----------------------------')
		print(' - Continuo con il programma -')

		print('--------------FINE PARTITA NUM:', matchCount)
		#SE i binanchi vincono, ho w.
		#esiti ha 9 spazi (indice fino 8)
		esiti = [0,0,0,0,0,0,0,0,0]
		calcoloIndice = (3 * hScelta) + hSceltaB 
		if result=='w': # VINTA
			#win[hScelta] = win[hScelta] + 1
			hPoint[hScelta] = hPoint[hScelta] + 10
			hPointB[hSceltaB] = hPointB[hSceltaB] -10
			esiti[calcoloIndice] = numTurno
		elif result=='l': # SCONFITTA
			#lost[hScelta] = lost[hScelta] + 1
			hPoint[hScelta] = hPoint[hScelta] - 10
			hPointB[hSceltaB] = hPointB[hSceltaB] + 10
			esiti[calcoloIndice] = -numTurno
		elif result=='x': # PATTA
			#draw[hScelta] = draw[hScelta] + 1
			hPoint[hScelta] = hPoint[hScelta] - 1
			hPointB[hSceltaB] = hPointB[hSceltaB] -1
			esiti[calcoloIndice] = 1
		stat.append(esiti)
		del esiti
		# aumentiamo il punteggio delle euristiche non usate.
		for i in range(0,3):
			if i != hScelta:
				hPoint[i] = hPoint[i]+2
			if i != hSceltaB:
				hPointB[i] = hPoint[i]+2

		numTurno = 0
		#######################################################################################
		# Bianco = Lettera Grande, Nero = Lettera minuscola

		if matchCount == 40:
			RisultatoFinale = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # 0 - 17  ||| DA 0 a 8 BIANCHI ;; da 9 a 17 NERI- 18 a 26
			mediaMosse = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			tipoStringa = ['Minimax vs Minimax','Minimax vs AlphaBeta Pruning','Minimax vs Negamax','AlphaBeta Pruning vs Minimax','AlphaBeta Pruning vs AlphaBeta Pruning','AlphaBeta Pruning vs Negamax','Negamax vs Minimax','Negamax vs AlphaBeta Pruning','Negamax vs Negamax']
			#Ho bisogno prima di tutto di una var per ogni tipo di euristica
			for x in stat:
				print('UNO per X stat')
				for n,y in enumerate(x):
					print(y)
					if y != 0:
						print(y)
						if y < 1:
							print('- minore ')
							#Vince NERO - moltiplica x2 indice
							indx = 9+n
							print(RisultatoFinale[indx])
							RisultatoFinale[indx] = RisultatoFinale[indx] + 1 

							mediaMosse[indx] = mediaMosse[indx] + (y*-1)
						elif y > 1:
							print('- maggiore ')
							print(RisultatoFinale[n])
							RisultatoFinale[n] = RisultatoFinale[n] + 1 
							#Vince Bianco - indice va bene così
							mediaMosse[n] = mediaMosse[n] + y
						else:
							print('- patta ')
							#Patta
							indx = 18+n
							print(RisultatoFinale[indx])
							RisultatoFinale[indx] = RisultatoFinale[indx] + 1 

			print(' Fine delle partite: Ecco i risultati finali ---')
			print('################################################')
			print(' Elenco delle prestazioni per ogni euristica:')
			print(' [Bianco] vs [Nero]')
			for i in range(0,9):
				print('****-> ' , tipoStringa[i],' <-****')
				print(' _____________________________________________________________ ')
				print(' Win = ',RisultatoFinale[i],'|| Lost = ',RisultatoFinale[i+9],'|| Draw = ',RisultatoFinale[i+18])
				if RisultatoFinale[i] == 0:
					mediaA = 0
				else:
					mediaA = mediaMosse[i]/RisultatoFinale[i]
				if RisultatoFinale[i+9] == 0:
					mediaB = 0
				else: 
					mediaB =mediaMosse[i+9]/RisultatoFinale[i+9]

				print(' Win Media mosse: ',mediaA , '|| Lost Media Mosse: ', mediaB )
				print(' _____________________________________________________________ ')

			break
		else:
			print(':::: MOSTRO LA SITUAZIONE ALLA PARTITA NUM ', matchCount,' ::::')
			print(' Per ogni euristica mostro Vittorie, Sconfitte, Pareggi/Patte')
			print('@@@@@@@')
			print(' Minimax -> ', win[0], ' - ', lost[0], ' - ', draw[0])
			print('@@@@@@@')
			print(' Minimax con alphaBeta Pruning -> ', win[1], ' - ', lost[1], ' - ', draw[1])
			print('@@@@@@@')
			print(' Negamax -> ', win[2], ' - ', lost[2], ' - ', draw[2])
			print('@@@@@@@')
			matchCount += 1

print('FINE')
