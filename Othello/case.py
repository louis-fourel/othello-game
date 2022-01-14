
class Case :
    """ Représente une case sur la grille """

    couleur = str   # transparent (par défaut) / noir / blanc
    coordonnees = tuple  # (X,Y) coordonee de la case sur la grille

    def __init__(self,coordonnees):
        self.couleur = 'transparent'
        self.coordonnees = coordonnees

    def setCouleur(self, couleur) :
        self.couleur = couleur
    
    def swapCouleur(self) :
        if self.couleur == 'noir' :
            self.couleur = 'blanc'
        else : 
            self.couleur = 'noir'




