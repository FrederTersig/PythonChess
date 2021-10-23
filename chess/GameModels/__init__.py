#!/usr/local/bin/python
'''
@author: Federico Tersigni
'''
import copy
#from test.test_dis import outer
#     POP 
class ChessRepresentation:
	
	def __init__(self, dict, wp, bp,wpos,bpos):

		if dict is None:
			
			self.board = {}
			self.whitePos = {} # contiene SOLO coordinate e tipo dei pezzi bianchi
			self.blackPos = {} # contiene SOLO coordinate e tipo dei pezzi neri
			self.whitePieces = {'t' : 2, 'c' : 2 , 'a' : 2, 'd' : 1 , 'r' : 1, 'p' : 8} 
			self.blackPieces = {'t' : 2, 'c' : 2 , 'a' : 2, 'd' : 1 , 'r' : 1, 'p' : 8}
			# prima i bianchi
			for x in range(0,8):
				for y in range(0,8):
					#Settaggio dei pezzi sulla scacchiera
					if x == 0:
						if y == 0 or y == 7:
							#Torre -----
							self.board[x,y] = 'tbn'
							self.blackPos[x,y] = 't'
						elif y == 1 or y == 6:
							#Cavallo
							self.board[x,y] = 'cbn'
							self.blackPos[x,y] = 'c'
						elif y == 2 or y == 5:
							#Alfiere
							self.board[x,y] = 'abn'
							self.blackPos[x,y] = 'a'
						elif y == 3:
							#Donna
							self.board[x,y] = 'dbn'
							self.blackPos[x,y] = 'd'
						else:
							#Re
							self.board[x,y] = 'rbn'
							self.blackPos[x,y] = 'r'
					elif x == 1:
						#Tutti Pedoni nella seconda riga
						self.board[x,y] = 'pbn'
						self.blackPos[x,y] = 'p'
					elif x > 1 and x < 6:
						self.board[x,y] = '0'
					elif x == 6:
						self.board[x,y] = 'pwn'
						self.whitePos[x,y] = 'p'
					else:
						if y == 0 or y == 7:
							#Torre
							self.board[x,y] = 'twn'
							self.whitePos[x,y] = 't'
						elif y == 1 or y == 6:
							#Cavallo
							self.board[x,y] = 'cwn'
							self.whitePos[x,y] = 'c'
						elif y == 2 or y == 5:
							#Alfiere
							self.board[x,y] = 'awn'
							self.whitePos[x,y] = 'a'
						elif y == 3:
							#Donna
							self.board[x,y] = 'dwn'
							self.whitePos[x,y] = 'd'
						else:
							#Re
							self.board[x,y] = 'rwn'
							self.whitePos[x,y] = 'r'
		else:
			self.board = dict  # è un dizionario!
			self.whitePieces = wp
			self.blackPieces = bp            
			self.whitePos = wpos
			self.blackPos = bpos
				
					
	def getBoard(self):
		return copy.deepcopy(self.board)
		


	def getPiece(self,x,y):
		try: 
			return self.board[x,y]
		except KeyError:
			if (x in range(0,8)) and (y in range(0,8)):
				return ''
			return None
		
	def checkPiece(self,x,y,tipo):
		if x < 0 or x > 7:
			#print('*x')
			return False
		if y < 0 or y > 7:
			#print('*y')
			return False

		if self.board[x,y] == '0' or len(self.board[x,y]) == 1:
			return False
		else:
			return self.board[x,y][0]==tipo
	
	def getPieceTurn(self,x,y):
		try: 
			if self.board[x,y] == '0' or len(self.board[x,y]) == 1:
				return '0'
			else:
				return self.board[x,y][1]  # Mi serve la seconda lettera per vedere il turno
		except KeyError:
			if (x in range(0,8)) and (y in range(0,8)):
				return ''
			return None
	
	
	def hasMoved(self,x,y): # TRUE ha mosso, FALSE NON ha mosso
		if self.board[x,y] == '0' or len(self.board[x,y]) == 1:
			return False
		else:
			#print(' Mi da qui problema? ', self.board[x,y])
			return self.board[x,y][2] == 's'
	
		
	def checkEP(self,x,y): # la casella deve avere un pezzo sopra
		if self.board[x,y] == '0' or self.board[x,y][0] != 'p':
			return False
		else:
			return self.board[x,y][2] == 'e'
	# fine En Passant
	
	
	
	def isFree(self,x,y):
		if (x,y) in self.board:
			if self.board[x,y] == '0' or len(self.board[x,y]) == 1: # SE è vuoto, allora True
				return True
			else: 
				return False
		else:
			return False
		#return self.getPiece(x,y)==''
		
	def isOpposite(self,turn,x,y):  # Può essere fatto SOLO su di una casella che ha una pezzo
		piece = self.getPiece(x, y)
		
		if len(piece) > 1 and not piece == '0': 
			return not piece[1] == turn  # True solo se il turno è opposto a quello passato in argomento
		else:
			return False
		# Qui bisogna vedere se il turno seguente sia uguale al turno del pezzo che andiamo a checkare

	def isAmissible(self, configuration):
		return True    
	
	def getBlackPieces(self):
		out = copy.deepcopy(self.blackPieces)
		return out
	def getWhitePieces(self):
		out = copy.deepcopy(self.whitePieces)
		return out
	
	# --> Togliere le funzioni sul 'black king' 
	def getBlackDict(self):
		out = copy.deepcopy(self.blackPos)
		return out
	def getWhiteDict(self):
		out = copy.deepcopy(self.whitePos)
		return out

	def setBoard(self, board):
		self.board = board

	def removeEpPawn(self,vet,board,rBoard):
		out = copy.deepcopy(self.board)
		for x,y in vet:

			if not out[x,y] == '0':
				if out[x,y][2] == 'e':
					out[x,y] = out[x,y][0] + out[x,y][1] + 's'
			else:
				print('ERRORE, le coordinate di un pedone portano ad una casella vuota!?!?')
				#print(out[x,y])
				#print(x, '  -  ', y)
				#print(board)
				#print('---')
				#print(rBoard)
				#print('---')
				#print(vet)
				#print('-----------------')
		self.setBoard(out)

	# Quali sono le condizioni che ci dicono se il re è 'sicuro' ?
	# {Con la premessa che vengano date delle coordinate possibili, nel senso interne alla griglia}
	# !! Si controllano i pezzi dell'avversario.. quindi si vede se il turno è opposto
	# 1) Le coordinate nx ny non devono essere minacciate da un pedone
	# 2) Le coordinate nx/ny non devono essere minacciate da una torre
	# 3) Le coordinate nx/ny non devono essere minacciate da un alfiere
	# 4) Le coordinate nx/ny non devono essere minacciate da una regina
	# 5) Le coordinate nx/ny non devono essere minacciate da un cavallo
	# 6) Le coordinate nx/ny non devono essere minacciate dal Re Avversario
	# -- Nell'algoritmo si controllano le varie direzioni facendo diversi cicli. Dispersivo? Meglio altro?

	
	#Ho bisogno di una funzione che veda SE una generica casella sia o meno minacciata
	def castlingEmptyPathCheck(self,x,y,turn):
		if x <= 7 and x >= 0 and y <= 7 and y >= 0:
			d = {}  # Il dizionario dei pezzi è costituito da Tupla = Stringa. chiave(x,y) = Stringa di Riconoscimento
			
			if turn == 'b': # 'b' sta per BLACK
				#print('dict = dizionario BIANCO')
				d = self.getWhiteDict()
			elif turn == 'w': # 'w' sta per WHITE
				#print('dict = dizionario NERO')
				d = self.getBlackDict()
			else:
				print('ERRORE: IsKingSafe turno SCONOSCIUTO')
			#print('ISKINGSAFE chiamato da --> ', turn, ' |||| CHE STA CONTRO -->', opTurn)
			for k, v in d.items():
				#print('Cicliamo sul dizionario --> ' , k , ' - ', v)
				# k sarà la chiave-tupla che rappresenta le coordinate del pezzo nella griglia
				# v sarà il valore-STRINGA dell'elemento del dizionario
				ox = k[0] # x
				oy = k[1] # y
				movement = []
				#print('Prima le coordinate:',k,' ==> ', v)
				if v == 'p': # Il pedone può 'mangiare' solo in due caselle in base al suo schieramento (turno)
					if turn == 'b':  # <--- da controllare
						movement = [(-1,1), (-1,-1)]
					elif turn =='w':
						movement = [(1,1), (1,-1)]
					else:
						print('ERRORE: isKingSafe turno del pedone SCONOSCIUTO')
				elif v == 't':
					#print('movimento Torre')
					movement = self.movimentoTorre(ox,oy,turn)
					#print(movement)
				elif v == 'c':
					movement = [(-2,1), (-1,2), (1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
				elif v == 'a':
					#print('Movimento Alfiere')
					movement = self.movimentoAlfiere(ox,oy,turn)
					#print(movement)
				elif v == 'd':
					movement = self.movimentoTorre(ox,oy,turn) + self.movimentoAlfiere(ox,oy,turn)
					#print('MOVIMENTI DELLA REGINA!!!')
					#print(movement)
				elif v == 'r':
					#print('movimenti del re')
					movement = [(-1,1), (-1,-1), (1,1), (1,-1), (-1,0), (0,1), (1,0), (0,-1)]
				else:
					print('Errore ---> isKingSafe : v non presente nella lista!!!!')
		
				for tup in movement:
					#print(tup, '<--- TUPLA ORIGINARIA')

					#print(tup[0],tup[1],tup,'----->>>>>>')
					#if 
					ax = ox+tup[0]
					ay = oy+tup[1]
					if ax <= 7 and ax >= 0 and ay <= 7 and ay >= 0:

						if ax == x and ay == y:
							#print('Arrocco Negato: casella di movimento del re minacciata. Coordinate: ', x,' ', y)
							return False
		
			# movement = vettore di tuple che rappresentano le varie caselle in cui il pezzo preso in esame dalla ciclo
			# for appena girato
		return True


	#### NUOVA FUNZIONE IS KING SAFE
	# Funzione isKingSafe(self, nx, ny, turn): (Suppongo che NX e NY SIANO interne alla griglia)
	def isKingSafe(self,nx,ny,turn):  # Ritorna TRUE se è sicuro, FALSE altrimenti
		#print('Chiamato isKingSafe con i seguenti argomenti: ', nx, '-',ny,' turno: ', turn)
		d = {}  # Il dizionario dei pezzi è costituito da Tupla = Stringa. chiave(x,y) = Stringa di Riconoscimento
		
		if turn == 'b': # 'b' sta per BLACK
			#print('dict = dizionario BIANCO')
			d = self.getWhiteDict()
		elif turn == 'w': # 'w' sta per WHITE
			#print('dict = dizionario NERO')
			d = self.getBlackDict()
		else:
			print('ERRORE: IsKingSafe turno SCONOSCIUTO')
		#print('ISKINGSAFE chiamato da --> ', turn, ' |||| CHE STA CONTRO -->', opTurn)
		for k, v in d.items():
			#print('Cicliamo sul dizionario --> ' , k , ' - ', v)
			# k sarà la chiave-tupla che rappresenta le coordinate del pezzo nella griglia
			# v sarà il valore-STRINGA dell'elemento del dizionario
			ox = k[0] # x
			oy = k[1] # y
			movement = []
			#print('Prima le coordinate:',k,' ==> ', v)
			if v == 'p': # Il pedone può 'mangiare' solo in due caselle in base al suo schieramento (turno)
				if turn == 'b':  # <--- da controllare
					movement = [(-1,1), (-1,-1)]
				elif turn =='w':
					movement = [(1,1), (1,-1)]
				else:
					print('ERRORE: isKingSafe turno del pedone SCONOSCIUTO')
			elif v == 't':
				#print('movimento Torre')
				movement = self.movimentoTorre(ox,oy,turn)
				#print(movement)
			elif v == 'c':
				movement = [(-2,1), (-1,2), (1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
			elif v == 'a':
				#print('Movimento Alfiere')
				movement = self.movimentoAlfiere(ox,oy,turn)
				#print(movement)
			elif v == 'd':
				movement = self.movimentoTorre(ox,oy,turn) + self.movimentoAlfiere(ox,oy,turn)
				#print('MOVIMENTI DELLA REGINA!!!')
				#print(movement)
			elif v == 'r':
				#print('movimenti del re')
				movement = [(-1,1), (-1,-1), (1,1), (1,-1), (-1,0), (0,1), (1,0), (0,-1)]
			else:
				print('Errore ---> isKingSafe : v non presente nella lista!!!!')
	
			for tup in movement:
				#print(tup, '<--- TUPLA ORIGINARIA')

				#print(tup[0],tup[1],tup,'----->>>>>>')
				#if 
				ax = ox+tup[0]
				ay = oy+tup[1]

				# Nelle prove mi esce ax = -3 ?!?!?
				if ax <= 7 and ax >= 0 and ay <= 7 and ay >= 0:
					stringa = self.getPiece(ax, ay)
					#print('LA STRINGA ====>>> ',stringa)
					if stringa[0] == 'r' and stringa[1] == turn:
						#print('IL RE NON SI TROVA IN SICUREZZA, la colpa ---> ', v, ' -> Coordinate: ', ox,oy)
						#print('AX/AY --> ',ax,'/',ay,' ----- MOVIMENTO --> ', tup[0], '/',tup[1])
						#print('Dizionario Controllato: ', d)
						#print('I Due Dizionari presenti sono:')
						#print('BIANCO = ', self.getWhiteDict())
						#print('NERO = ',self.getBlackDict())
						return False
				#Il ramo else prende tutte quelle coordinate create dal cavallo e gli altri pezzi che non hanno movimenti ciclati
				#else:
				#    print(' HAI SBAGLIATO SIA TORRE CHE ALFIERE!!! pezzo = ', v,'coord:', ox,'/',oy, '>> coordinate mod: ', ax,'/',ay)
	
		# movement = vettore di tuple che rappresentano le varie caselle in cui il pezzo preso in esame dalla ciclo
		# for appena girato
		return True

	
	def movimentoAlfiere(self,ix,iy,turn):
		out = []
		i=1
		close = False
		# Variabili per sostituire ix-i e tutte le altre stronzate
		# bisogna semplificare a BESTIA questo codice, e usare la booleana CLOSE per chiudere il while e non fare qualche uscita di cazzo
		while not close: # ok
			if ix-i >= 0 and iy-i >= 0:
				stringa = self.getPiece(ix-i, iy-i)
				if stringa == '0':
					out.append((-i,-i))
					i = i + 1
				else:
					close = True
					if stringa[0] == 'r' and stringa[1] == turn: # SE è il re del TUO schieramento
						out.append((-i,-i))
					i = 1
			else: 
				close = True
		close = False
		i=1
		while not close: # controllare
			if ix+i <= 7 and iy+i <= 7:
				stringa = self.getPiece(ix+i, iy+i)
				if stringa == '0':
					out.append((+i,+i))
					i = i + 1 
				else:
					close = True
					
					if stringa[0] == 'r' and stringa[1] == turn: # SE è il re del TUO schieramento
						out.append((+i,+i))
					i = 1 
			else: 
				close = True
		close = False
		i=1
		while not close: # controllare
			if ix+i <= 7 and iy-i >= 0:
				stringa = self.getPiece(ix+i, iy-i)
				if stringa == '0':
					out.append((+i,-i))
					i = i + 1
				else:
					close = True
					if stringa[0] == 'r' and stringa[1] == turn: # SE è il re del TUO schieramento
						out.append((+i,-i))
					i = 1
			else: 
				close = True
			
		close = False
		i=1
		while not close: # forse ok
			if ix-i >= 0 and iy+i <= 7:
				stringa = self.getPiece(ix-i, iy+i)
				if stringa == '0':
					out.append((-i,+i))
					i = i + 1
				else:
					close = True
					if stringa[0] == 'r' and stringa[1] == turn: # SE è il re del TUO schieramento
						out.append((-i,+i))
					i = 1
			else: 
				close = True
			
		return out
		#Fine Funzione movimentoAlfiere
	
	
	def movimentoTorre(self,ix,iy,turn):# Modo per creare tutte le varie coordinate. 0 +-y ; +-x 0 ;
		# Ritorna un array di tuple che rappresentano le caselle in cui una torre può muoversi
		# crei un ciclo che mi vede passo passo se un passo è o no possibile
		out = []
		i=1
		close = False
		while not close:
			if iy-i >= 0:
				stringa = self.getPiece(ix,iy-i)
				if stringa == '0':
					out.append((0,-i))
					i = i + 1
				else:
					close = True
					if stringa[0] == 'r' and stringa[1] == turn:# SE è il re del TUO schieramento
						out.append((0,-i))
					i=1
					
			else:
				close = True
		close=False
		i=1
		while not close:
			if iy+i <= 7:
				stringa = self.getPiece(ix,iy+i)
				if stringa =='0':
					out.append((0,+i))
					i = i+1
				else:
				
					close = True
					if stringa[0] == 'r' and stringa[1] == turn:
						out.append((0,+i))
					i = 1
			else:
				close = True
		close = False
		i=1
		while not close:
			if ix+i <=7:
				stringa = self.getPiece(ix+i,iy)
				if stringa =='0':
					out.append((+i,0))
					i = i + 1
				else:
					close = True
				
					
					if stringa[0] == 'r' and stringa[1] == turn:
						out.append((+i,0))
					i = 1
			else: 
				close = True
		close = False
		i=1
		while not close:
			if ix-i >= 0:
				stringa = self.getPiece(ix-i,iy)
				if stringa =='0':
					out.append((-i,0))
					i = i + 1
				else:
					close = True
					
					if stringa[0] == 'r' and stringa[1] == turn:
						out.append((-i,0))
					i = 1
			else: 
				close = True
		return out
		#FiNE FUNZIONE TORRE
	
	####  
		# -1  0 | -2  0  SU
		# -1  1 | -2  2  SU/DX
		#  0  1 |  0  2  DX
		#  1  1 |  2  2  GIU/DX 
		#-----------------------|
		#  1  0 |  2  0  GIU
		#  1 -1 |  2 -2  GIU/SX
		#  0 -1 |  0 -2  SX
		# -1 -1 | -2 -2  SU/SX          
		##################################################################################################      
		
	def pieceMovement(self, x, y, piece, turn): # questo va benissimo
		movelist = set()
		#ricorda che viene data solo una lettera come argomento, senza vedere il turno
		
		# SE il re del proprio schieramento è minacciato, si possono fare soltanto mosse che liberano da questa condizione
		# IN QUESTA FUNZIONE AGISCE IL CONTROLLO DI 'SALVEZZA' DEL RE, CHE DEVE POTER SCARTARE GLI STATI CHE NON PERMETTONO
		# LA SALVAGUARDIA DEL RE
		# cambio da > if piece[0] == '0':||| a > if piece == '0':
		
		#if piece =='0':
		#    return movelist  # vuota
		#--------- C'ERA PERCHE' SI RIFERIVA ALLA GRIGLIA NON AL DIZIONARIO
		#print('ECCO PIECE MOVEMENT!!!!!!! -------------->', piece)
		if piece=='t':  # Mosse della torre (Orizzontale e Verticale)
			##############################################
			#print('MOVIMENTO DELLA TORRE')
			# opero sulla X
			if 7 - x > 0:
				#print('GIU')
				dif = 7 - x
				i = 1 # Giu
				while i <= dif: # da migliorare
					# creo la tupla usando la x ; + i , y
					if self.isFree(x+i,y):
						movelist.add((x+i,y))
					else:
						if self.isOpposite(turn, x+i, y):
							movelist.add((x+i,y))
						break
					i = i + 1
			# opero sulla X
			if x - 1 >= 0:
				#print('SU')
				dif = x - 1
				# Su
				while dif >= 0:
					# creo la tupla usando la x ; + i , y
					#print('Risultato di isFree --> ', self.isFree(dif,y))
					if self.isFree(dif,y):
						movelist.add((dif,y))
					else:                        
						#print('Risultato di isOpposite --> ',self.isOpposite(turn,dif,y))
						if self.isOpposite(turn,dif,y):
							movelist.add((dif,y))
						
						#print('invoco il BREAK per uscire')
						break
					#print('cambio DIF')
					dif = dif - 1
				#print('SONO USCITO')
			# opero sulla Y
			if 7 - y > 0:
				#print('DESTRA')
				dif = 7 - y
				i = 1
				# Destra
				while i <= dif: 
					#print('Risultato di isFree --> ', self.isFree(x,y+i))
					if self.isFree(x,y+i):
						movelist.add((x,y+i))
					else:
						if self.isOpposite(turn, x, y+i):
							movelist.add((x,y+i))
						#print('invoco il BREAK per uscire')
						break
					#print('SONO USCITO')
					i = i + 1
					
			if y - 1 >= 0:
				#print('SINISTRA')
				dif = y - 1
				flag = 0
				# Sinistra
				while dif >= 0:
					#print('Risultato di isFree --> ', self.isFree(x,dif))
					if self.isFree(x, dif):
						movelist.add((x, dif))
					else:
						if self.isOpposite(turn,x,dif):
							movelist.add((x, dif))
						#print('invoco il BREAK per uscire')
						break
					dif = dif - 1
		####################################################
		elif piece=='c':
			#print('movimento del cavallo')
			# movimento cavallo ----- 2, 1 !
			if x + 2 <= 7:
				if y + 1 <= 7:
					if self.isFree(x+2, y+1):
						movelist.add((x+2,y+1))
					else:
						if self.isOpposite(turn, x+2, y+1):
							movelist.add((x+2,y+1))
				if y - 1 >= 0:
					if self.isFree(x+2,y-1):
						movelist.add((x+2,y-1))
					else:
						if self.isOpposite(turn, x+2, y-1):
							movelist.add((x+2,y-1))
			if x - 2 >= 0:
				if y + 1 <= 7:
					if self.isFree(x-2,y+1):
						movelist.add((x-2,y+1))
					else:
						if self.isOpposite(turn, x-2, y+1):
							movelist.add((x-2,y+1))
				if y - 1 >= 0:
					if self.isFree(x-2,y-1):
						movelist.add((x-2,y-1))
					else:
						if self.isOpposite(turn, x-2, y-1):
							movelist.add((x-2,y-1))
			if y + 2 <= 7:
				if x + 1 <= 7:
					if self.isFree(x+1,y+2):
						movelist.add((x+1,y+2))
					else:
						if self.isOpposite(turn, x+1, y+2):
							movelist.add((x+1,y+2))
				if x - 1 >= 0:
					if self.isFree(x-1,y+2):
						movelist.add((x-1,y+2))
					else:
						if self.isOpposite(turn, x-1, y+2):
							movelist.add((x-1,y+2))
			if y - 2 >= 0:
				if x + 1 <= 7:
					if self.isFree(x+1,y-2):
						movelist.add((x+1,y-2))
					else:
						if self.isOpposite(turn, x+1, y-2):
							movelist.add((x+1,y-2))
				if x - 1 >= 0:
					if self.isFree(x-1,y-2):
						movelist.add((x-1,y-2))
					else:
						if self.isOpposite(turn, x-1, y-2):
							movelist.add((x-1,y-2))
				
		elif piece =='a':
			# movimento alfiere
			# GIU DESTRA
			#print('movimento alfiere')
			if 7-x > 0 and 7 - y > 0:
			
				difx = 7 - x
				dify = 7 - y 
				i = 1
				while i <= difx and i <= dify:
					if self.isFree(x+i,y+i):
						movelist.add((x+i,y+i))
					else:
						if self.isOpposite(turn,x+i,y+i):
							movelist.add((x+i,y+i))
						break
					i = i + 1
		
			if x -1 >= 0 and y-1 >= 0: # CORRETTO -> SU SINISTRA
				difx = x-1
				dify = y-1
				while difx >= 0 and dify >= 0:
					if self.isFree(difx,dify):
						movelist.add((difx,dify))
					else:
						if self.isOpposite(turn,difx, dify):
							movelist.add((difx,dify))
						break
					difx = difx - 1
					dify = dify - 1
					
			if 7-x > 0 and y - 1 >= 0:
				difx = 7 - x
				dify = y - 1
				i = 1
				while i <= difx and dify >= 0:
					if self.isFree(x+i,dify):
						movelist.add((x+i, dify))
					else:
						if self.isOpposite(turn,x+i, dify):
							movelist.add((x+i, dify))
						break
					i = i + 1
					dify = dify - 1
					
			if x - 1 >= 0 and 7-y > 0:
				difx = x - 1
				dify = 7 - y
				i = 1
				while difx >= 0 and i <= dify:
					if self.isFree(difx,y+i):
							movelist.add((difx, y+i))
					else:
						if self.isOpposite(turn,difx, y+i):
							movelist.add((difx, y+i))
						break
					i = i + 1
					difx = difx - 1

		elif piece == 'd': #########################################################
			#print('movimento donna')
			#print('MOVIMENTO DELLA TORRE')
			if 7 - x > 0:
				dif = 7 - x
				i = 1
				# Giu
				while i <= dif: # da migliorare
					# creo la tupla usando la x ; + i , y
					if self.isFree(x+i,y):
						movelist.add((x+i,y))
					else:
						if self.isOpposite(turn, x+i, y):
							movelist.add((x+i,y))
						break
					i = i + 1

			if x - 1 >= 0:
				dif = x - 1
				# Su
				while dif >= 0:
					# creo la tupla usando la x ; + i , y
					if self.isFree(dif,y):
						movelist.add((dif,y))
					else:                        
						if self.isOpposite(turn,dif,y):
							movelist.add((dif,y))
						break
					dif = dif - 1
			if 7 - y > 0:
				dif = 7 - y
				i = 1
				# Destra
				while i <= dif: 
					if self.isFree(x,y+i):
						#print('LIBERA')
						movelist.add((x,y+i))
					else:
						#print('NON LIBERA')
						if self.isOpposite(turn, x, y+i):
							movelist.add((x,y+i))
						break
					i = i + 1
					
			if y - 1 >= 0:
				dif = y - 1
				# Sinistra
				while dif >= 0:
					if self.isFree(x, dif):
						movelist.add((x, dif))
					else:
						if self.isOpposite(turn,x,dif):
							movelist.add((x, dif))
						break
					dif = dif - 1
			# movimento alfiere
			#print('MOVIMENTO ALFIERE')
			# GIU DESTRA
			
			if 7-x > 0 and 7 - y > 0:
			
				difx = 7 - x
				dify = 7 - y 
				i = 1
				while i <= difx and i <= dify:
					if self.isFree(x+i,y+i):
						movelist.add((x+i,y+i))
					else:
						if self.isOpposite(turn,x+i,y+i):
							movelist.add((x+i,y+i))
						break
					i = i + 1
		
			if x -1 >= 0 and y-1 >= 0: # CORRETTO -> SU SINISTRA
				difx = x-1
				dify = y-1
				while difx >= 0 and dify >= 0:
					if self.isFree(difx,dify):
						movelist.add((difx,dify))
					else:
						if self.isOpposite(turn,difx, dify):
							movelist.add((difx,dify))
						break
					difx = difx - 1
					dify = dify - 1
					
			if 7-x > 0 and y - 1 >= 0:
				difx = 7 - x
				dify = y - 1
				i = 1
				while i <= difx and dify >= 0:
					if self.isFree(x+i,dify):
						movelist.add((x+i, dify))
					else:
						if self.isOpposite(turn,x+i, dify):
							movelist.add((x+i, dify))
						break
					i = i + 1
					dify = dify - 1
					
			if x - 1 >= 0 and 7-y > 0:
				difx = x - 1
				dify = 7 - y
				i = 1
				while difx >= 0 and i <= dify:
					if self.isFree(difx,y+i):
							movelist.add((difx, y+i))
					else:
						if self.isOpposite(turn,difx, y+i):
							movelist.add((difx, y+i))
						break
					i = i + 1
					difx = difx - 1
			######################################## <<<---- Da qui bisogna ripulire ancora i 'getPieceTurn'
		elif piece == 'r': ## IS KING SAFE DA CORREGGERE :: manca lo stato
			#print('movimento re')
			# movimento Re
			if x + 1 <= 7:            
				if self.isFree(x+1, y): # La casella è vuota ? 
					movelist.add((x+1,y))  # Allora questa è una mossa possibile
				else: # SE la casella non è vuota
					if self.isOpposite(turn,x+1, y): # La casella ha un pezzo dello schieramento diverso?
						movelist.add((x+1,y))  # Allora questa è una mossa possibile, MANGIA
			if x - 1 >= 0:
				if self.isFree(x-1,y):
					movelist.add((x-1,y))
				else:
					if self.isOpposite(turn,x-1,y):
						movelist.add((x-1,y))
						
			if y + 1 <= 7:
				if self.isFree(x,y+1):
					movelist.add((x,y+1))
				else:
					if self.isOpposite(turn,x, y+1):
						movelist.add((x,y+1))
						
			if y - 1 >= 0:                 
				if self.isFree(x,y-1):
					movelist.add((x,y-1))
				else:
					if self.isOpposite(turn,x,y-1):
						movelist.add((x,y-1))
					
			# Diagonali
			if x - 1 >= 0 and y - 1 >= 0:                 
				if self.isFree(x-1,y-1):
					movelist.add((x-1,y-1))
				else:
					if self.isOpposite(turn,x-1,y-1):
						movelist.add((x-1,y-1))
					
			if x - 1 >= 0 and y + 1 <= 7:
				if self.isFree(x-1,y+1):
						movelist.add((x-1,y+1))
				else:
					if self.isOpposite(turn,x-1,y+1):
						movelist.add((x-1,y+1))
						
			if x + 1 <= 7 and y - 1 >= 0:
					
				if self.isFree(x+1,y-1):
					movelist.add((x+1,y-1))
				else:
					if self.isOpposite(turn,x+1,y-1):
						movelist.add((x+1,y-1))
					
			if x + 1 <= 7 and y + 1 <= 7:
				if self.isFree(x+1,y+1):
					movelist.add((x+1,y+1))
				else:
					if self.isOpposite(turn,x+1,y+1):
						movelist.add((x+1,y+1))
			# Arrocco ------------------------------------------------------------
			if self.canCastlingLeft(x, y, turn):
				# Sposta re di due a sinistra e torre di tre a destra ---> Ricorda che inserisci APPOSTA le coordinate del re o della torre
				if self.checkPiece(x, y, 't'):
					movelist.add((x,y+4))
				elif self.checkPiece(x,y,'r'):
					movelist.add((x,y-4))
			if self.canCastlingRight(x, y, turn):
				# Sposta re di due a destra, sposta torre di due a sinistra    
				if self.checkPiece(x, y, 't'):
					movelist.add((x,y-3))
				elif self.checkPiece(x,y,'r'):
					movelist.add((x,y+3))
			#------------------------------------------------------------------------
		else:  # PEDONE  -------------- ULTIMA PARTE DA CORREGGERE         
			# IL MOVIMENTO DEL PEDONE CHE MANGIA PER EN PASSANT NON PREVEDE DUE POSSIBILI EN PASSANT MA UNO SOLO
			# SE turn Black, il pedone muove con x+;  
			# Se turn White, il pedone muove con x-;
			if turn == 'b' and x+1 <= 7:
				#Nel caso dei neri, x+1 = 5 perché il pedone e.p. si trova a x=4 insieme al pedone nero
				if self.isFree(x+1,y):
					movelist.add((x+1,y))
				if x==4: #per poter mangiare un pedone che usa EnPassant, deve trovarsi in x=4
					if y+1<=7 and self.checkEP(x,y+1) and self.isOpposite(turn,x,y+1) and self.isFree(x+1,y+1):
						#print('############################################# MOVIMENTO PEDONE PREVEDE MANGIATA EN PASSANT NERO DESTRA')
						movelist.add((x+1,y+1)) # Mangio per enPassant
					elif y-1>=0 and self.checkEP(x,y-1) and self.isOpposite(turn,x,y-1) and self.isFree(x+1,y-1):
						#print('############################################# MOVIMENTO PEDONE PREVEDE MANGIATA EN PASSANT NERO SINISTRA')
						movelist.add((x+1,y-1)) # Mangio per enPassant
				# ------------- Mangia pedina di fazione opposta che si trova in diagonale 
				if y+1<=7 and not self.isFree(x+1,y+1) and self.isOpposite(turn,x+1,y+1):
					movelist.add((x+1,y+1)) # Mangio NORMALMENTE
				if y-1>=0 and not self.isFree(x+1,y-1) and self.isOpposite(turn,x+1,y-1):
					movelist.add((x+1,y-1)) # Mangio NORMALMENTE
				# ------------- Se è il primo movimento, può muoversi in En Passant
				if x+2 <= 7 and self.isFree(x+1,y) and self.isFree(x+2,y) and not self.hasMoved(x,y) and not self.checkEP(x,y):
					movelist.add((x+2,y))
			elif turn =='w' and x-1 >= 0:
				#Nel caso dei bianchi, x-1 = 2 perché il pedone e.p si trova a x=3 insieme al pedone bianco
				if self.isFree(x-1,y):
					movelist.add((x-1,y))
				if x==3: #per poter mangiare un pedone nero e.p., il pedone bianco deve trovarsi in x=3
					if y+1<=7 and self.checkEP(x,y+1) and self.isOpposite(turn,x,y+1) and self.isFree(x-1,y+1):
						#print('############################################# MOVIMENTO PEDONE PREVEDE MANGIATA EN PASSANT BIANCO DESTRA')
						movelist.add((x-1,y+1))
					elif y-1>=0 and self.checkEP(x,y-1) and self.isOpposite(turn,x,y-1) and self.isFree(x-1,y-1):    
						#print('############################################# MOVIMENTO PEDONE PREVEDE MANGIATA EN PASSANT BIANCO SINISTRA')
						movelist.add((x-1,y-1))
				# ------------- Mangia pedina di fazione opposta che si trova in diagonale 
				if y+1<=7 and not self.isFree(x-1,y+1) and self.isOpposite(turn,x-1,y+1):
					movelist.add((x-1,y+1)) # mangio NORMALMENTE
				if y-1>=0 and not self.isFree(x-1,y-1) and self.isOpposite(turn,x-1,y-1):
					movelist.add((x-1,y-1)) # mangio NORMALMENTE
				# ------------- Se è il primo movimento, può muoversi in En Passant
				if x-2 >=0 and self.isFree(x-1,y) and self.isFree(x-2,y) and not self.hasMoved(x,y) and not self.checkEP(x,y):
					movelist.add((x-2,y))

		return movelist       
	
	# Funzione per il controllo della possibilità di arrocco
	# Castling è la traduzione in inglese di Arrocco - La funzione ritorna una Booleana.

	# Castling da modificare: la mossa conta solo per il re non per la torre.


	#Arrocco di Destra
	def canCastlingRight(self,x,y,turn):
		
		prima = self.getPiece(x,y) # Prendo la stringa presente in quella posizione della griglia
		
		if prima[0]=='r' and not prima[2]=='s':
			if self.isFree(x,y+1) and self.isFree(x,y+2) and not self.isFree(x,y+3): # Si potrebbe aggiungere 'y+3 è torre dello stesso schieramento?'
				seconda = self.getPiece(x,y+3)
				if seconda[0]=='t' and not seconda[2]=='s':
					if self.isKingSafe(x,y,turn) and self.castlingEmptyPathCheck(x,y+1,turn) and self.castlingEmptyPathCheck(x,y+2,turn):
					#if self.isKingSafe(x,y,turn) and self.isKingSafe(x,y+1,turn) and self.isKingSafe(x,y+2,turn):
						return True
					#Ultima condizione, is king safe deve controllare

		#if prima[0]=='r' and not prima[2]=='s': # SE è un re e non ha mai mosso
		#	if self.isFree(x,y+1) and self.isFree(x,y+2) and not self.isFree(x,y+3): # Le caselle che si frappongono devono essere libere
		#		seconda = self.getPiece(x,y+3)
		#		if seconda[0]=='t' and not seconda[2]=='s': # SE è una torre e non ha mai mosso
		#			if self.isKingSafe(x,y,turn) and self.isKingSafe(x,y+1,turn) and self.isKingSafe(x,y+2,turn):
		#				#SE il re non si trova minacciato in xy,y+1,y+2
		#				return True
		#elif prima[0]=='t' and not prima[2]=='s':
		#	if self.isFree(x,y-1) and self.isFree(x,y-2) and not self.isFree(x,y-3):
		#		seconda = self.getPiece(x,y-3)
		#		if seconda[0]=='r' and not seconda[2]=='s':
		#			if self.isKingSafe(x,y-1,turn) and self.isKingSafe(x,y-2,turn) and self.isKingSafe(x,y-3,turn):
		#				#il re non è minacciato? allora ok!
		#				return True
	
		return False
	
	# Arrocco di Sinistra
	def canCastlingLeft(self,x,y,turn):
		


		prima = self.getPiece(x,y)
		if prima[0]=='r' and not prima[2]=='s': # Condizione giusta
			if self.isFree(x,y-1) and self.isFree(x,y-2) and self.isFree(x,y-3) and not self.isFree(x,y-4): # 3 caselle si frappongono a sinistra!
				seconda = self.getPiece(x,y-4) # DA VEDERE
				if seconda[0]=='t' and not seconda[2]=='s':
					if self.isKingSafe(x,y,turn) and self.castlingEmptyPathCheck(x,y-1,turn) and self.castlingEmptyPathCheck(x,y-2,turn):
					#if self.isKingSafe(x,y,turn) and self.isKingSafe(x,y-1,turn) and self.isKingSafe(x,y-2,turn):
						return True
		#elif prima[0]=='t' and not prima[2]=='s':
		#	if self.isFree(x,y+1) and self.isFree(x,y+2) and self.isFree(x,y+3) and not self.isFree(x,y+4):
		#		seconda = self.getPiece(x,y+4)
		#		if seconda[0]=='r' and not seconda[2]=='s':
		#			if self.isKingSafe(x,y+2,turn) and self.isKingSafe(x,y+3,turn) and self.isKingSafe(x,y+4,turn):
		#				return True
		return False
		
class chessState(object):
	
	def __init__(self,heuristic, dict, wp, bp,wpos, bpos):
		self.H = heuristic
		self.representation = ChessRepresentation(dict,wp,bp,wpos,bpos)
	
	def getBoard(self):
		return self.representation.getBoard()

	def setBoard(self,board):
		return self.representation.setBoard(board)
	
	def getBlackPieces(self):
		return self.representation.getBlackPieces()
	def getWhitePieces(self):
		return self.representation.getWhitePieces()
	
	def getBlackDict(self):
		return self.representation.getBlackDict()
	
	def getWhiteDict(self):
		return self.representation.getWhiteDict()
		
	def checkBoard(self):
		return self.representation.checkBoard()
	def getPiece(self, x,y):
		return self.representation.getPiece(x, y)  

	def removeEpPawn(self,vet,board,rBoard):
		return self.representation.removeEpPawn(vet,board,rBoard)
	
	def hasMoved(self,x,y):
		self.representation.hasMoved(x, y)
	   
	def getPieceTurn(self,x,y):
		return self.representation.getPieceTurn(x,y)
	
	def isFree(self,x,y):
		return self.representation.isFree(x, y)
	
	def isOpposite(self,turn,x,y):
		return self.representation.isOpposite(turn, x, y)
	
	def getPieceValue(self, lettera):
		return self.representation.getPieceValue(lettera)
	
	def checkEP(self,x,y):
		return self.representation.checkEP(x, y)
	
	def checkPiece(self,x,y,tipo):
		return self.representation.checkPiece(x, y, tipo)   
	def castlingEmptyPathCheck(self,x,y,turn):
		return self.representation.castlingEmptyPathCheck(x,y,turn)
	
	def isKingSafe(self,nx,ny,turn):
		return self.representation.isKingSafe(nx, ny, turn)
	
	def pieceMovement(self,x,y,piece,turn):
		return self.representation.pieceMovement(x, y, piece, turn)
				
				
class Game:
	
	def __init__(self, initialState=None, heuristic=None):
		self.state = initialState
		self.heuristic = heuristic

	def neighbors(self, state):
		out = set([])  # Un set di stati può andare bene?
		return out

	def getState(self):
		return self.state
	
	def setState(self,state):
		self.state = state

	def solution(self, state):
		return True
	
class ChessGame(Game):
	
	def __init__(self,heuristic):
		self.state = chessState(heuristic,None,None,None,None,None)
		
	def setMove(self,x,y, dict): # la casella deve essere occupata da un pezzo
		#Questa funzione mi permette di segnare un pezzo che si è mosso almeno una volta
		out = copy.deepcopy(dict)  # out sarebbe la copia del dizionario che prendiamo in argomento
		stringa = out[x,y][0] + out[x,y][1] + 's' 
		out[x,y]=stringa
		return out # Mi ritorna un dizionario uguale a quello passato in argomento solo con quella modifica fatta
	
	def setMovement(self,x,y,dict): # la casella deve avere un pezzo sopra
		out = copy.deepcopy(dict)
		out[x,y] = out[x,y][0] + out[x,y][1] + 's'
		return out # Mi ritorna un dizionario
	
	# EP = En Passant
	def setEP(self,x,y,dict): # la casella deve avere un pezzo sopra
		out = copy.deepcopy(dict)
		stringa = out[x,y][0] + out[x,y][1] + 'e' 
		out[x,y] = stringa
		return out
		
	def checkState(self,board): # FUNZIONE PER LA VISUALIZZAZIONE DELLA GRIGLIA
		cont = 0
		for c in range(8): # SCRIVO I NUMERI SUPERIORI E INFERIORI
			if c == 0:
				print('   ', end ='')
				print(c, end=' ')
			else:
				print(' ', end='')
				print(c, end=' ')
		print()
		for x in range(8):
			print(cont,end='-')
			for y in range(8):
				print('[', end='') # APRE
				if board[x,y] == None or board[x,y] == '0' or board[x,y] == '':
					print('0', end='')
				else:
					if board[x,y][1] == 'w':
						print((str(board[x,y][0]).upper()), end='')
					else:
						print((str(board[x,y][0])), end='')
				print(']', end='') # CHIUDE
				
			print('-', end=str(cont))
			print() # Manda a capo dopo la y
			cont += 1
		for c in range(8): # SCRIVO I NUMERI SUPERIORI E INFERIORI
			if c == 0:
				print('   ', end ='')
				print(c, end=' ')
			else:
				print(' ', end='')
				print(c, end=' ')
		print()
		#print('------ Mostro Pedoni ---------')
		#prova = list( (board[x,y],x,y) for x,y in board if board[x,y][0] == 'p' or board[x,y][0] == 'P')
		#print(prova)

	def checkPieces(self,wp,bp):
		print('WHITEPIECES==>',wp)
		print('BLACKPIECES==>',bp)
		
	def reducePieces(self,piece, dict):
		#diminuisce il numero di pezzi nel dizionario
		#print('reducePieces chiamato per ridurre ==> ', piece)
		out = copy.deepcopy(dict)
		out[piece] = out[piece]-1
		return out
	
	def addPieces(self,piece,dict): # da controllare
		# aggiunge un pezzo nel dizionario specifico
		out = copy.deepcopy(dict)
		out[piece] = out[piece]+1
		return out
	
	def setPiece(self, x, y, piece,dict): # OTTIMO, NON c'è bisogno di un pezzo sopra la casella
		
		out = copy.deepcopy(dict)
		out[x,y] = piece
		return out  # Ritorna il dizionario con quelle specifiche modifiche
	
	# Funzione setPiecePos per cambiare la sua posizione nel dizionario white/blackPos
	def setPiecePos(self,x,y,xe,ye,dict):
		#print('setPiecePos')
		out = copy.deepcopy(dict)
		try:
			stringa = out[x,y]
			del out[x,y]
			out[xe,ye] = stringa
			
			#out[xe,ye] = out.pop(x,y)
		except KeyError as ex:
			print('SetPiecePos Non esiste questa chiave : ', ex)
			#print('NEL SEGUENTE DIZIONARIO::::')
			#print(out)
			#print('----')
		return out
	
	#Funzione delPiecePos per cancellare il pezzo nel dizionario white/blackPos
	
	def delPiecePos(self,x,y,dict,prova):
		#print('delPiecePos')
		out = copy.deepcopy(dict)
		try:
			del out[x,y]
		except KeyError as ex:
			print('DelPiecePos Non esiste questa chiave : ', ex)
			#print('NEL SEGUENTE DIZIONARIO::::')
			#print(out)
			#print('----')
			#print(prova)
			#print('----')
		return out
	
	
	# COSA DEVE FARE LA FUNZIONE DI UPGRADE DEL PEDONE?
	# 1) MI CONTROLLA SE LA X DEL PEDONE E' 7 O 0 IN BASE AL TURNO CORRENTE
	# 2) O CHIEDE DI SCEGLIERE LA PEDINA AL GIOCATORE OPPURE CREA UNO STATO DIVERSO PER OGNI PEZZO CHE PUO' SCEGLIER
	# 3) CREA L'EFFETTIVO STATO SUGGERITO
	
	#def upgradePCPawn(self,x,y,wp): # Funzione del computer
	#    print('miao')

	def upgradePlayerPawn(self): # Funzione per 'upgradare' il pedone
		#print('upgradePlayerPawn!!')
		scelta = ''
		flag = 0
		while flag == 0:
			print('# SCEGLI IL PEZZO PER LA PROMOZIONE DEL PEDONE #')
			choose = str(input('# a = alfiere; d = donna ; t = torre, c = cavallo #\n'))
			try:
				print('Hai scelto :', choose)
				if choose == 'a' or choose == 'd' or choose == 't' or choose == 'c':
					flag = 1
					scelta = choose
				else:
					print('# SCELTA NON VALIDA! Reinserisci il pezzo!! #')
			except ValueError:
				print('# non hai inserito un testo, riprova! #')

		return scelta

	def moving(self, state,x,y,xn,yn,turn): # RITORNA UN SOLO STATO
		#print('moving, quale turno?', turn)
			
		dict = copy.deepcopy(self.makeMove(state, x, y, xn, yn))
		wnumber = copy.deepcopy(state.representation.whitePieces)
		bnumber = copy.deepcopy(state.representation.blackPieces)
		
		if turn == 'w': # NON E' DA CAMBIARE!!
			bpos = copy.deepcopy(state.representation.blackPos)
			wpos = self.setPiecePos(x,y,xn,yn,state.representation.whitePos)
		else:
			bpos = self.setPiecePos(x,y,xn,yn,state.representation.blackPos)
			wpos = copy.deepcopy(state.representation.whitePos)
				
		#CREA LO STATO E RITORNALO
		# Fai l'upgrade del pedone
		# le funzioni ritornano le liste da  sostituire alle WhitePieces e BlackPieces
		out = chessState(state.H, dict, wnumber, bnumber,wpos,bpos)
		return out
	
	def doEP(self,state,x,y,xn,yn,turn):
		#print('###########################################doEP, quale turno?', turn)
		dict = self.makeMove(state,x,y,xn,yn) # Muovo la pedina oltre il pedone mangiato per en-passant		
		wnumber = state.getWhitePieces()
		bnumber = state.getBlackPieces()
		bpos = state.getBlackDict() #pos
		wpos = state.getWhiteDict() #pos

		if turn == 'b': # Black, x crescente
			#print('Vogliamo togliere un elemento White Pos : ', wpos[x,yn])
			# Elimino l'elemento dallo schieramento avversario
			del wpos[x,yn] #l'elemento si trova a fianco del pedone X,Y
			wnumber = self.reducePieces('p',wnumber)
			# Cambio le coordinate del pedone nero nello schieramento dei neri
			bpos = self.setPiecePos(x,y,xn,yn,state.getBlackDict())
		else: # White, y decrescente
			#print('Vogliamo togliere un elemento Black Pos : ', bpos[x,yn])
			# Elimino l'elemento dallo schieramento avversario
			del bpos[x,yn] #l'elemento si trova a fianco del pedone X,Y
			bnumber = self.reducePieces('p',bnumber)

			# Cambio le coordinate del pedone bianco nello schieramento dei bianchi
			wpos = self.setPiecePos(x,y,xn,yn,state.getWhiteDict())

		#print(' Elemento nella griglia che abbiamo eliminato ---> ', dict[x,yn])
		# Tolgo il pedone MANGIATO, per poi rimuoverlo anche dalla griglia
		del dict[x,yn]
		dict[x,yn] = '0' 
		# Dopo aver fatto tutto, creo un nuovo stato e lo ritorno     		
		out = chessState(state.H, dict, wnumber, bnumber,wpos,bpos)
		return out
	
	def doEat(self, state, x, y, xe, ye,turn): # RITORNA UN SOLO STATO
		pezzo = state.getPiece(xe,ye)[0] # Registro il tipo di pezzo che si trova in XE / YE 
		grid = self.makeMove(state, x, y, xe, ye) # Muovo la pedina X Y verso XE YE
		
		#Quando mangiamo, dobbiamo cancellare il pezzo SIA dalla griglia, dal pos e dal pieces.
		
		wnumber = copy.deepcopy(state.representation.whitePieces)
		bnumber = copy.deepcopy(state.representation.blackPieces)
		
		if not grid[xe,ye] == '0' and not grid[xe,ye] == '':
			if turn == 'w': # NON E' DA CAMBIARE
				#Riduco il numero di pedoni dell'avversario (nero)
				bnumber = copy.deepcopy(self.reducePieces(pezzo,bnumber))

				#Cambio le coordinate del pedone nero che si sposta in diagonale.
				wpos = self.setPiecePos(x,y,xe,ye, state.representation.whitePos)
				bpos = self.delPiecePos(xe,ye,state.representation.blackPos,state.representation.board)
				
			else: 
				#print('Pezzi mangiati dai neri: Prima e Dopo')
				#print('Il turno di chi riduciamo i pezzi -', turn)
				wnumber = copy.deepcopy(self.reducePieces(pezzo,wnumber))
				#Setto la modifica dei dizionari 'pos' > Bianco mangiato e nero spostato
				bpos = self.setPiecePos(x,y,xe,ye,state.representation.blackPos)
				wpos = self.delPiecePos(xe,ye, state.representation.whitePos, state.representation.board)
		else:
			print(' ERRORE DO EAT --> il pezzo di arrivo = vuoto')      
		# Dopo aver tolto il pezzo che mangio, posso cambiare la pedina:
		grid = self.setMove(xe, ye, grid) # Il pezzo che si è mosso, quindi se è la prima mossa
		out = chessState(state.H, grid, wnumber, bnumber,wpos,bpos)
		#print('STATO DOPO-----------')
		#self.checkState(out.representation.board)
		#self.checkPieces(out.representation.whitePos, out.representation.blackPos)
		#print('_--------------_')
		return out
	
	def doCastlingSwitch(self,diz,x,y,ox,oy): # mi cambia i dizionari nell'arrocco
		count = len(diz)
		
		if count == 64:
			if diz[ox,oy]=='0': #---> DEVE essere per forza 0 se è griglia
				#Si tratta della griglia!
				pezzo = diz[x,y]
				diz[x,y] = '0' # Diventa vuoto!
				diz[ox,oy] = pezzo
			else:
				#Si tratta di white/black POS
				pezzo = diz[x,y]
				del diz[x,y]
				diz[ox,oy] = pezzo
		else:
			pezzo = diz[x,y]
			del diz[x,y]
			diz[ox,oy] = pezzo

		
		return diz
	
	# Funzione che permette di realizzare una mossa, spostando la pedina da una coordinata all'altra
	def makeMove(self,state,x,y,xn,yn): # Dato uno stato, posizione base e posizione nuova si vede se si può spostare e si ritorna
		#print('makeMove trigger!')
		arrocco = False
		grid = copy.deepcopy(state.representation.board) # mi serve la griglia dello stato passato in argomento
	
		if not state.isFree(x,y): #Esiste la pedina? 
			if not state.hasMoved(x,y): #Se la terza lettera della pedina NON è una S (mai mosso o e.p.)
				
				if state.checkPiece(x,y,'p') and abs(x-xn) == 2 and not state.checkEP(x,y): #Se il pedone muove di due = e.p. 
					grid = self.setEP(x,y,grid)
					
				elif state.checkPiece(x,y,'r') and abs(y-yn) == 2: #Re e arrocco
					grid = self.setMove(x,y,grid)
					pr = state.getPiece(x,y) #Per fare lo spostamento mi serve il tipo del pezzo
					grid = self.setPiece(x,y,'0',grid)
					grid = self.setPiece(xn,yn,pr,grid)
					
					if y - yn == -2 and state.checkPiece(x,y+3,'t'):
						#Arrocco di destra
						grid = self.setMove(x,y+3,grid)
						pt = state.getPiece(x,y+3) #Per fare lo spostamento mi serve il tipo del pezzo
						grid = self.setPiece(x,y+3,'0',grid)
						grid = self.setPiece(x,y-1,pt,grid) # Controllo per nuove coordinate?
	
					if y-yn == 2 and state.checkPiece(x,y-4,'t'):
						#Arrocco di sinistra
						grid = self.setMove(x,y-4,grid)
						pt = state.getPiece(x,y-4) #Per fare lo spostamento mi serve il tipo del pezzo
						grid = self.setPiece(x,y-4,'0',dict)
						grid = self.setPiece(x,y-1,pt,grid) # Controllo per nuove coordinate?
					else: 
						print('ERRORE MAKEMOVE --> ARROCCO &&& RE ')
				elif state.checkPiece(x,y,'t') and y - yn == 3:
					arrocco = True # L'arrocco avvenuto
				elif state.checkPiece(x,y,'p') and state.checkEP(x,y): #Pedone enPassant, il turno dopo torna normale (terza lettera s)
					grid = self.setMove(x,y,grid)
				else: #Se è una qualsiasi altra pedina
					grid = self.setMove(x,y,grid)
			
		else:
			print('ERRORE --- makeMove: Le coordinate originali x,y non rappresentano un pezzo ma uno spazio vuoto')
	
		if not arrocco: 
			piece = grid[x,y]
			grid = self.setPiece(x,y,'0',grid)
			grid = self.setPiece(xn,yn,piece,grid)
		return grid
	
	def checkKing(self,state,dict,turn): # Per checkare direttamente la posizione del re: Bisogna proteggerlo sempre e fare mosse che non lo espongano.
		for key, value in dict.items():
			#print('-- Check King : Cosa abbiamo qui? ')
			#print(' key, value : ', key, ' | ', value)
			if value == 'r':
				#print('Un re in checkKing -- ', key[0],key[1])
				#print('----------------------' , key)
				return state.isKingSafe(key[0],key[1],turn)

		return None	
		#king = list(dict.keys())[list(dict.values()).index('r')]
		#grid = state.getBoard()
		#print('Check del re dello schieramento --> ', turn, ' // Queste sono le sue coordinate attuali: ', king[0],'/',king[1])
		#return state.isKingSafe(king[0],king[1],turn) 
	
	
	def checkWin(self,state,dict):
		for key,val in dict.items():
			if val == 'r':
				return False
		return True

	def checkDraw(self,state):
		wDict = state.getWhitePieces()
		bDict = state.getBlackPieces()
		comp= False
		count = 0
		# PRIMA DI TUTTO -> Check se rimane RE vs RE o RE vs ALF/RE o RE vs CAV/RE
		for key,val in wDict.items():
			if val != 'a' or val != 'c' and key > 0:
				return False
			if val == 'a' or val == 'c' and key > 1:
				return False
			if val == 'a' or val == 'c' and key == 1:
				count +=1


		if count > 1:
			return False
		else:
			count = 0
			comp = True

		for key,val in bDict.items():
			if comp == True:
				if val != 'r' and key > 0:
					return False
			else:
				if val != 'a' or val != 'c' and key > 0:
					return False
				if val == 'a' or val == 'c' and key > 1:
					return False
				if val == 'a' or val == 'c' and key == 1:
					count +=1
		if count > 1:
			return False

		###########################################################
		#SE non viene mai ritornato falso, ritorna True : partita 'patta'
		return True


	def remEpPawn(self, vet, board):
		out = copy.deepcopy(board)
		for x,y in vet:

			if not out[x,y] == '0':
				if out[x,y][2] == 'e':
					out[x,y] = out[x,y][0] + out[x,y][1] + 's'
			else:
				print('ERRORE, le coordinate di un pedone portano ad una casella vuota!?!?')
				print(out[x,y])
				print(x, '  -  ', y)
				print(board)
				print('---')
				print(rBoard)
				print('---')
				print(vet)
				print('-----------------')
		return out

	#MODIFICATA, CHECKALA
	def neighbors(self,turn,state):

		out = set()
		if turn=='w':
			# prendo i pezzi bianchi
			dict = state.getWhiteDict()
			listaPedoni = [z for z in dict if dict.get(z) == 'p']

			if len(listaPedoni) > 0:
				#state.removeEpPawn(listaPedoni, dict, state.getBoard())
				state.setBoard(self.remEpPawn(listaPedoni,state.getBoard()))

			for x,y in dict:
				piece = dict[x,y]

				if not state.isFree(x,y): #è davvero una pedina?
					move = state.pieceMovement(x,y,piece,'w')
					for m in move:
						xn,yn = m[0],m[1]
						if xn <= 7 and xn >= 0 and yn <= 7 and yn >= 0:
						#Cicliamo ogni mossa che ha la pedina selezionata

							if state.isFree(xn,yn): #Va verso una casella vuota?
								#Prima di tutto: Mangiata enPassant
								if state.checkPiece(x,y,'p') and state.checkPiece(x,yn,'p') and state.checkEP(x,yn) and state.getPieceTurn(x,yn) != 'w':
									#Posso mangiare Pedone EnPassant avversario che si trova alla destra del mio pedone -affamato-
									#print('********************** TURNO: White')
									#print(' Appena prima di En Passant: Mostro stati PRIMA::')
									#self.checkState(state.getBoard())
									#print('*****')
									#print(state.getWhiteDict())
									#print('****')
									#print(' [[IMPORTANTE - la board deve essere diversa da quella che si presenta dopo]]')
									if yn - y == 1: # DESTRA
										#print('Un pedone bianco vuole mangiare un pedone nero EN Passant che sta alla destra')
										ns = self.doEP(state, x, y, xn, yn, 'w')
										if self.checkKing(ns,dict,'w'):
											out.add(ns)
											#self.checkState(ns.getBoard())
											#print('****')
											#print(ns.getWhiteDict())
											#print('****')
										del ns
									elif yn - y == -1:
										#print('un pedone bianco vuole mangiare un pedone nero EN Passant che sta alla sinistra')
										ns = self.doEP(state, x, y, xn, yn, 'w')
										if self.checkKing(ns,dict,'w'):
											out.add(ns)
											#self.checkState(ns.getBoard())
											#print('****')
											#print(ns.getWhiteDict())
											#print('****')
										del ns
									#print('******************')
								else:
									ns = self.moving(state,x,y,xn,yn,'w') # moving mi invoca makemove che cambia la sigla della pedina.
									if self.checkKing(ns,dict,'w'):     
										#Upgrado il pedone del computer
										if ns.checkPiece(xn,yn,'p') and xn==0:
											#print('upgrade in corso:  .  .  .')
											morph = ['a','d','t','c']
											old = ns.getPiece(xn,yn)
											wPieces = ns.getWhitePieces() # Dizionario dei pezzi
											bPieces = ns.getBlackPieces()
											wPieces['p'] = wPieces['p'] - 1
											wPos = ns.getWhiteDict()
											bPos = ns.getBlackDict()
											del wPos[xn,yn] # Cancello il pedone in bPos
											
											for l in morph:
												pezzo = l + old[1] + old[2]
												nPezzo = self.setPiece(xn,yn,pezzo,ns.getBoard())
												# bPieces
												xPieces = self.addPieces(l, wPieces)
												xPos = copy.deepcopy(wPos)
												xPos[xn,yn] = l
												nSt = chessState(state.H, nPezzo,xPieces,bPieces,xPos,bPos)
												out.add(nSt)
												del pezzo,nPezzo,xPieces,xPos,nSt
										else:
											out.add(ns)				
									del ns
							#SE la coordinata non è libera e soprattutto è occupata da una pedina dello schieramento opposto
							elif not state.isFree(xn,yn) and not state.getPieceTurn(xn,yn) == 'w':
								ns = self.doEat(state,x,y,xn,yn,'w')
								if self.checkKing(ns,dict,'w'):
									# Upgrade pedone del computer    
									#XXX
									if ns.checkPiece(xn,yn,'p') and xn==0:     
										#print('Upgrade in corso:  .  .  .')
										morph = ['a','d','t','c']
										old = ns.getPiece(xn,yn)
										wPieces = ns.getWhitePieces() # Dizionario dei pezzi
										bPieces = ns.getBlackPieces()
										wPieces['p'] = wPieces['p'] - 1
										wPos = ns.getWhiteDict()
										bPos = ns.getBlackDict()
										del wPos[xn,yn] # Cancello il pedone in bPos
										
										for l in morph:
											pezzo = l + old[1] + old[2]
											nPezzo = self.setPiece(xn,yn,pezzo,ns.getBoard())
											# bPieces
											xPieces = self.addPieces(l, wPieces)
											#xPieces = copy.deepcopy(bPieces)
											#xPieces[l] = xPieces[l] + 1
											# bPos
											xPos = copy.deepcopy(wPos)
											xPos[xn,yn] = l
											nSt = chessState(state.H, nPezzo,xPieces,bPieces,xPos,bPos)
											out.add(nSt)
											del pezzo,nPezzo,xPieces,xPos,nSt
									else:
										out.add(ns)
								del ns
							elif not state.isFree(xn,yn) and state.getPieceTurn(xn,yn) == 'w' and x == xn:
								#Tentativo di arrocco? Se è un re, xn yn puntano ad una torre
								if dict[xn,yn] == 't' and dict[x,y]=='r':
									diz = copy.deepcopy(dict)
									brd = copy.deepcopy(state.getBoard())
									if abs(y-yn)==4: #arrocco alla regina
										#dict[x,y] è un re - lo muovo di 2
										diz = self.doCastlingSwitch(diz, x, y, x, y-2)
										brd = self.doCastlingSwitch(brd,x,y,x,y-2)
										stringaA = brd[x,y-2][0] + brd[x,y-2][1] + 's' 
										brd[x,y-2]=stringaA
										# Torre di 3
										diz = self.doCastlingSwitch(diz,xn,yn,xn,yn+3)
										brd = self.doCastlingSwitch(brd,xn,yn,xn,yn+3)
										stringaB = brd[xn,yn+3][0]
									elif abs(y-yn)==3: #Arrocco alfiere
										#Torre a y-2
										diz = self.doCastlingSwitch(diz, x, y, x, y+2)
										brd = self.doCastlingSwitch(brd,x,y,x,y+2)
										stringaA = brd[x,y+2][0] + brd[x,y+2][1] + 's' 
										brd[x,y+2]=stringaA
										#Re a y+2   # --- > CREO MOLTEPLICI COPIE DEI DIZIONARI :: SOLUZIONE PER FARLO SOLO UNA VOLTA?
										diz = self.doCastlingSwitch(diz,xn,yn,xn,yn-2)
										brd = self.doCastlingSwitch(brd,xn,yn,xn,yn-2)
										stringaB = brd[xn,yn-2][0] + brd[xn,yn-2][1] + 's' 
										brd[xn,yn-2]=stringaB
									else:
										print('ERRORE: neighbors arrocco sbagliato')

									# Quindi abbiamo brd = griglia, diz = dizionario BLACK --
									diz_b = state.getBlackDict()
									
									wPies = state.getWhitePieces() # Dizionario dei pezzi
									bPies = state.getBlackPieces()
									
									ns = chessState(state.H, brd,wPies,bPies,diz,diz_b)
									out.add(ns)
									del wPies,bPies,ns,stringaA,stringaB,diz,brd
						else:
							print('Errore:Neighbors- Dovrebbe essere stata selezionata una pedina ma in realtà è una casella vuota')
						del xn,yn
					del move
				del piece

				#### FINE parte bianchi / white.
		elif turn =='b':
			dict = state.getBlackDict()
			listaPedoni = [z for z in dict if dict.get(z) == 'p']

			if len(listaPedoni) > 0:
				#print(listaPedoni)
				#state.removeEpPawn(listaPedoni, dict, state.getBoard())
				state.setBoard(self.remEpPawn(listaPedoni,state.getBoard()))
			for x,y in dict:
				piece = dict[x,y]

				if not state.isFree(x,y): #è davvero una pedina?
					move = state.pieceMovement(x,y,piece,'b')
					for m in move:
						xn,yn = m[0],m[1]
						if xn <= 7 and xn >= 0 and yn <= 7 and yn >= 0:
						#Cicliamo ogni mossa che ha la pedina selezionata

							if state.isFree(xn,yn): #Va verso una casella vuota?
								#Prima di tutto: Mangiata enPassant
								if state.checkPiece(x,y,'p') and state.checkPiece(x,yn,'p') and state.checkEP(x,yn) and state.getPieceTurn(x,yn) != 'b':
									#Posso mangiare Pedone EnPassant avversario che si trova alla destra del mio pedone -affamato-
									#print('********* TURNO = BLACK')
									#print(' Appena prima di En Passant: Mostro stati PRIMA::')
									#self.checkState(state.getBoard())
									#print('****')
									#print(state.getBlackDict())
									#print('****')
									#print(' [[IMPORTANTE - la board deve essere diversa da quella che si presenta dopo]]')

									if yn - y == 1: # DESTRA
										#print('- Un pedone nero mangia EP Bianco alla sua destra : ', x,',',y)
										ns = self.doEP(state, x, y, xn, yn, 'b')
										if self.checkKing(ns,dict,'b'):
											out.add(ns)
											#self.checkState(ns.getBoard())
											#print('****')
											#print(ns.getBlackDict())
											#print('****')
										del ns
									elif yn - y == -1:
										#print('- Un pedone nero mangia EP Bianco alla sua sinistra: ', x,',',y)
										ns = self.doEP(state, x, y, xn, yn, 'b')
										if self.checkKing(ns,dict,'b'):
											out.add(ns)
											#self.checkState(ns.getBoard())
											#print('****')
											#print(ns.getBlackDict())
											#print('****')
										del ns
									#print('*********')
								else:
									ns = self.moving(state,x,y,xn,yn,'b') # moving mi invoca makemove che cambia la sigla della pedina.
									if self.checkKing(ns,dict,'b'):     
										#Upgrado il pedone del computer
										if ns.checkPiece(xn,yn,'p') and xn==7:
											#print('upgrade in corso:  .  .  .')
											morph = ['a','d','t','c']
											old = ns.getPiece(xn,yn)
											wPieces = ns.getWhitePieces() # Dizionario dei pezzi
											bPieces = ns.getBlackPieces()
											bPieces['p'] = bPieces['p'] - 1
											wPos = ns.getWhiteDict()
											bPos = ns.getBlackDict()
											del bPos[xn,yn] # Cancello il pedone in bPos
											
											for l in morph:
												pezzo = l + old[1] + old[2]
												nPezzo = self.setPiece(xn,yn,pezzo,ns.getBoard())
												# bPieces
												xPieces = self.addPieces(l, bPieces)
												xPos = copy.deepcopy(bPos)
												xPos[xn,yn] = l
												
												nSt = chessState(state.H, nPezzo,wPieces,xPieces,wPos,xPos)
												out.add(nSt)
												del pezzo,nPezzo,xPieces,xPos,nSt
										else:
											out.add(ns)
											
									del ns
							#SE la coordinata non è libera e soprattutto è occupata da una pedina dello schieramento opposto
							elif not state.isFree(xn,yn) and not state.getPieceTurn(xn,yn) == 'b':
								#print('sto per mangiare qualcosa !?')
								ns = self.doEat(state,x,y,xn,yn,'b')
								if self.checkKing(ns,dict,'b'):
									# Upgrade pedone del computer    
									if ns.checkPiece(xn,yn,'p') and xn==7:     
										#print('Upgrade in corso:  .  .  .')
										morph = ['a','d','t','c']
										old = ns.getPiece(xn,yn)
										wPieces = ns.getWhitePieces() # Dizionario dei pezzi
										bPieces = ns.getBlackPieces()
										bPieces['p'] = bPieces['p'] - 1
										wPos = ns.getWhiteDict()
										bPos = ns.getBlackDict()
										del bPos[xn,yn] # Cancello il pedone in bPos
										
										for l in morph:
											pezzo = l + old[1] + old[2]
											nPezzo = self.setPiece(xn,yn,pezzo,ns.getBoard())
											# bPieces
											xPieces = self.addPieces(l, bPieces)
											#xPieces = copy.deepcopy(bPieces)
											#xPieces[l] = xPieces[l] + 1
											# bPos
											xPos = copy.deepcopy(bPos)
											xPos[xn,yn] = l
											
											nSt = chessState(state.H, nPezzo,wPieces,xPieces,wPos,xPos)
											out.add(nSt)
											del pezzo,nPezzo,xPieces,xPos,nSt
									else:
										out.add(ns)
								del ns
							elif not state.isFree(xn,yn) and state.getPieceTurn(xn,yn) == 'b' and x == xn:
								#Tentativo di arrocco? Se è un re, xn yn puntano ad una torre
								if dict[xn,yn] == 't' and dict[x,y]=='r':
									diz = copy.deepcopy(dict)
									brd = copy.deepcopy(state.getBoard())
									if abs(y-yn)==4: #arrocco alla regina
										#dict[x,y] è un re - lo muovo di 2
										diz = self.doCastlingSwitch(diz, x, y, x, y-2)
										brd = self.doCastlingSwitch(brd,x,y,x,y-2)
										stringaA = brd[x,y-2][0] + brd[x,y-2][1] + 's' 
										brd[x,y-2]=stringaA
										# Torre di 3
										diz = self.doCastlingSwitch(diz,xn,yn,xn,yn+3)
										brd = self.doCastlingSwitch(brd,xn,yn,xn,yn+3)
										stringaB = brd[xn,yn+3][0]
									elif abs(y-yn)==3: #Arrocco alfiere
										#Torre a y-2
										diz = self.doCastlingSwitch(diz, x, y, x, y+2)
										brd = self.doCastlingSwitch(brd,x,y,x,y+2)
										stringaA = brd[x,y+2][0] + brd[x,y+2][1] + 's' 
										brd[x,y+2]=stringaA
										#Re a y+2   # --- > CREO MOLTEPLICI COPIE DEI DIZIONARI :: SOLUZIONE PER FARLO SOLO UNA VOLTA?
										diz = self.doCastlingSwitch(diz,xn,yn,xn,yn-2)
										brd = self.doCastlingSwitch(brd,xn,yn,xn,yn-2)
										stringaB = brd[xn,yn-2][0] + brd[xn,yn-2][1] + 's' 
										brd[xn,yn-2]=stringaB
									else:
										print('ERRORE: neighbors arrocco sbagliato')

									# Quindi abbiamo brd = griglia, diz = dizionario BLACK --
									diz_w = state.getWhiteDict()
									
									wPies = state.getWhitePieces() # Dizionario dei pezzi
									bPies = state.getBlackPieces()
									
									ns = chessState(state.H, brd,wPies,bPies,diz_w,diz)
									out.add(ns)
									del wPies,bPies,ns,stringaA,stringaB,diz,brd
						else:
							print('Errore:Neighbors- Dovrebbe essere stata selezionata una pedina ma in realtà è una casella vuota')
						del xn,yn
					del move
				del piece
		return out