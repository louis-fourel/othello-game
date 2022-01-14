import random

class Joueur :

    def __init__(self, nom, couleur, is_IA=False):
        self.nom = nom
        self.couleur = couleur
        self.nbPoints = 0
        self.is_IA = is_IA
    
    def jouer_coup_IA(self, grille, skill=1):
        if skill == 1:
            return grille.convertCoord(random.choice(list(grille.coupsPossibles.keys())))

 
