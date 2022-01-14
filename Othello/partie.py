from os import system
from time import sleep

from joueur import Joueur
from grille import Grille
from moteur import Moteur
 
class Partie :

    def __init__(self) :

        print("\nNouvelle partie !\n")
        nomJoueur1 = input("Qui joue les blancs ?  ")
        nomJoueur2 = input("Ok ! Qui joue les noirs ?  ")
        self.joueur1 = Joueur(nomJoueur1, 'noir', is_IA=True)
        self.joueur2 = Joueur(nomJoueur2, 'blanc')
        joueur_actif = self.joueur1
        joueur_non_actif = self.joueur2

        self.moteur = Moteur(joueur_actif, joueur_non_actif, Grille(26))

    def whoWin(self):
        for c in self.moteur.grille.cases.flatten():
            if c.couleur == self.joueur1.couleur :
                self.joueur1.nbPoints += 1
            if c.couleur == self.joueur2.couleur :
                self.joueur2.nbPoints += 1
        
        np1 = self.joueur1.nbPoints
        np2 = self.joueur2.nbPoints

        print ("\n~~~ Fin de la partie ~~~\n")
        if np1 - np2 != 0:
            winner = self.joueur1 if np1 > np2 else self.joueur2
            print (f"{winner.nom} a gagné !\n")

        else:
            print (f":-O ! Egalité les cocos !\n")
        print (f"~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__" :

    print("\n*** Bienvenue dans l'Othello du Turfu ! ***\n")

    partie = Partie()
    
    skip_turn = False

    while (partie.moteur.grille.isNotFull()) :

        partie.moteur.update_cases_dispo()

        for case_coord in partie.moteur.grille.coupsPossibles:
            partie.moteur.grille.cases[case_coord].couleur = 'transparent'
        partie.moteur.grille.coupsPossibles.clear()
        partie.moteur.coups_joueur_actif()

        if not partie.moteur.grille.coupsPossibles :
            if skip_turn:
                break

            skip_turn = True

            print(f"\n\n:-( Malheureusement, pas de coup possible pour {partie.moteur.joueur_actif.nom} :-(")
            partie.moteur.changer_actif()
            print(f"C'est de nouveau à {partie.moteur.joueur_actif.nom} de jouer."),
            for i in range(3):
                sleep(1)
                print("."),
            continue

        skip_turn = False
  
        partie.moteur.grille.afficherGrille()
        
        isCoupJouable = False
        isFirstIter = True


        while not isCoupJouable :
            if isFirstIter :
                if partie.moteur.joueur_actif.is_IA:
                    coup = partie.moteur.joueur_actif.jouer_coup_IA(partie.moteur.grille)
                    sleep(1)
                    print(f'\n{partie.moteur.joueur_actif.nom} a joué : {coup}')
                    # sleep(1)
                else:
                    coup = input(f"\nQuel coup pour {partie.moteur.joueur_actif.nom} ?  ")
                isFirstIter = False
            else : 
                coup = input(f"\n{partie.moteur.joueur_actif.nom}, il faut choisir une case disponible ! Quelle case te fait envie ?  ")
            
            coordCoup = partie.moteur.grille.convertCoord(coup)
            isCoupJouable = partie.moteur.verif_coup_jouable(coordCoup)

        if not partie.moteur.joueur_actif.is_IA:
                system('clear')
        partie.moteur.jouer(coordCoup)
        partie.moteur.changer_actif()

    partie.moteur.grille.afficherGrille()
    partie.whoWin()
