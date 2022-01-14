import copy
import math
 
#move, evaluation = minimax(board, 8, -math.inf, math.inf, True)

def minimax(grille, depth, alpha, beta, joueur, maximizing_player):

    if depth == 0 or not grille.isNotFull():
        return None, evaluate(grille,joueur)


    children = list(grille.coupsPossibles.keys())
    best_move = children[0]
    
    if maximizing_player:
        max_eval = -math.inf        
        for child in children:
            grille_copy = copy.deepcopy(grille)

            # Jouer le coup sur la nouvelle grille

            

            current_eval = minimax(grille_copy, depth - 1, alpha, beta, False)[1]
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = child
            alpha = max(alpha, current_eval)
            if beta <= alpha:
                break
        return best_move, max_eval

    else:
        min_eval = math.inf
        for child in children:
            grille_copy = copy.deepcopy(grille)

            # Jouer le coup sur la nouvelle grille

            current_eval = minimax(grille_copy, depth - 1, alpha, beta, True)[1]
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = child
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        return best_move, min_eval

def evaluate(grille, joueur):
    return grille.nbPion(joueur)
