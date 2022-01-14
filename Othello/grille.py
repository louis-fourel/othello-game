from os import system
import numpy as np
from case import Case
import string

class Grille:

    def __init__(self, taille) : 
        
        if taille > 26 :
            self.taille = 26
        else :
            self.taille = taille

        self.cases = np.array([[Case((i,j)) for j in range(self.taille)]
                                for i in range(self.taille)])

        self.pions = []
        #for coord in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        for coord in [(3, 3), (3, 4), (4, 3), (4, 4)]:
            if sum(coord)%2 == 0:
                self.cases[coord].couleur = 'blanc'
            else:
                self.cases[coord].couleur = 'noir'
            self.pions.append(coord)

        # self.cases[3, 3].couleur = 'blanc'
        # self.cases[3, 4].couleur = 'noir'
        # self.cases[4, 3].couleur = 'noir'
        # self.cases[4, 4].couleur = 'blanc'

        self.cases_dispo = []
        self.coupsPossibles = {}


    def afficherGrille(self) :

        #system('clear')
        #print(list(map(lambda x: (x.coordonnees, x.couleur), self.cases.flatten())))

        dicoSymbole = {'transparent' : " ", 'noir' : "X", "blanc" : "O", "jouable" : "."}
        lettres = [lettre for lettre in string.ascii_uppercase[:self.taille]]
        lettres = '   '.join(lettres)
        ligneLettres = '\n      '+lettres       
        print(ligneLettres)

        ligneSeparation = "    "+"+---"*self.taille+"+"
        
        print(ligneSeparation)

        listTypeCase = []
        ligneFinal = ''
        for i in range(self.taille) :
            listTypeCase.clear()
            ligneFinal=''
            for j in range(self.taille) :
                for c in self.cases.flatten():
                    if c.coordonnees == (i, j) :
                        listTypeCase.append(dicoSymbole[c.couleur])

            ligneFinal = " | ".join(listTypeCase)
            print(f" {i:2d} | {ligneFinal} |")
            print(ligneSeparation)

    def isNotFull(self): 
        isNotFull = False
        for c in self.cases.flatten():
            if c.couleur in ('transparent', 'jouable'):
                isNotFull = True
        return isNotFull

    def convertCoord(self, coup):
        if type(coup) == tuple:
            result = string.ascii_uppercase[coup[1]] + str(coup[0])
        if type(coup) == str:
            result = (int(coup[1]),ord(coup[0])-65)
        return result

    def is_in_grid(self, coord) :
        if ((coord[0] >= 0 and coord[0] < self.taille) and (coord[1] >= 0 and coord[1] < self.taille)) :
            return True
        else :
            return False

    def nbPion(self, joueur) :
        count = 0
        for c in self.cases.flatten():
            if c.couleur == joueur.couleur :
                count +=1
        return 

        




