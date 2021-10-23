'''
@author: Federico Tersigni
'''
import math

class Heuristic:
    def __init__(self):
        pass

    def H(self, state):
        return 1

class ChessHeuristic(Heuristic):
    def getPieceValue(self, lettera):
        value = 0  # il valore del pezzo principale : il pedone.
        if lettera == 't':
            value = 5
        elif lettera == 'c' or lettera == 'a':
            value = 3
        elif lettera == 'd':
            value = 9
        elif lettera == 'p':
            value = 1
        else:  # Se si tratta del 're'.
            value = 500
        
        return value
    
    def H0(self, state): # Ci restituisce il valore euristico del nodo
        # number of whites - number of blacks
        out = 0
        # Bianco cerca minore
        # SE wp maggiore di bp (SE bianchi hanno più pedine), totale PICCOLO

        # Nero cerca Maggiore
        # SE bp maggiore di wp (SE neri hanno più pedine), totale GRANDE 
        wp = state.getWhitePieces()  # NON DEVO MODIFICARE
        bp = state.getBlackPieces()  # NON DEVO MODIFICARE
        for key in wp: # white
            valore = self.getPieceValue(key) * wp[key] # Il valore derivante dal pezzo esaminato
            #print('--', valore)
            out = out - valore
        for key in bp: # black
            valore = self.getPieceValue(key) * bp[key]
            out = out + valore
            # Nero
        #print(out, ' <--- Valore totale euristica')
        return out

    #Minimax Heuristic (Zero-sum)
    def H1(self, game, state, l, turn):
        # SE stiamo a profondità 0 O se è un nodo terminale
        if l == 0 or game.checkWin(state, state.getBlackDict()) or game.checkWin(state, state.getWhiteDict()):
            return self.H0(state)

        if turn == 'w': # Alfa + infinito
            alpha = +10000
            for x in game.neighbors(turn,state):
                if x is not None:
                    alpha = min(alpha, self.H1(game, x, l-1, 'b'))
        else:
            alpha = -10000
            for x in game.neighbors(turn,state):
                if x is not None:
                    alpha = max(alpha, self.H1(game, x, l-1, 'w'))
        return alpha

    # Minimax con Alfabeta Pruning ::
    #h2(self,game,state,l,-1000,+1000,turn)
    def H2(self,game,state,l,alpha,beta,turn):
        if l == 0 or game.checkWin(state, state.getBlackDict()) or game.checkWin(state, state.getWhiteDict()):
            return self.H0(state)
        if turn == 'b': # SE MASSIMIZZA
            val = -10000
            for x in game.neighbors('b',state):
                
                val = max(val, self.H2(game, x, l-1,alpha,beta, 'w'))
                alpha = max(alpha, val)
                if beta <= alpha:
                    break #Interrompi il ciclo
            return val
        elif turn == 'w': # SE MINIMIZZA
            val = 10000
            for x in game.neighbors('w',state):
            
                val = min(val, self.H2(game, x, l-1,alpha,beta, 'b'))
                beta = min(beta, val)
                if beta <= alpha:
                    break # Interrompi il ciclo
            return val    
    
    def H3(self,game,state,l,alpha,beta,turn):
        if turn == 'w':
            p = 1
        else:
            p = -1
        return self.negamax(game,state,l,alpha,beta,p)

    def negamax(self,game,state,l,alpha,beta,p):
        if l==0:
            return p * self.H0(state)
        else:
            if p == 1:
                turn = 'w'
            else:
                turn = 'b'
            #v = -math.inf
            for x in game.neighbors(turn,state):
                #v = max(v, -self.negamax(game,x,l-1,-beta,-alpha,-p))
                alpha = max(alpha,-self.negamax(game,x,l-1,-beta,-alpha,-p))
                if alpha >= beta:
                    return beta
                    break
            
        return alpha


    


        
