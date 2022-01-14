class Moteur:
    dico_directions = {'NO':(-1, -1),
                       'N':(-1, 0),
                       'NE':(-1, 1),
                       'E':(0, 1),
                       'SE':(1, 1),
                       'S':(1, 0),
                       'SO':(1, -1),
                       'O':(0, -1)}
 
    def __init__(self, joueur_actif, joueur_non_actif, grille) -> None:
        self.joueur_actif = joueur_actif
        self.joueur_non_actif = joueur_non_actif
        self.grille = grille
        return

    def coups_joueur_actif(self) -> None:
        for case_coord in self.grille.cases_dispo:
            case = self.grille.cases[case_coord]
            temp = [self.check_dir(case, direction, [])
                             for direction in Moteur.dico_directions.values()]
            dir_possibles = [item for sublist in temp for item in sublist]
            
            if dir_possibles:
                case.couleur = 'jouable'
                self.grille.coupsPossibles[case_coord] = dir_possibles
        return
    
    def check_dir(self, case_init, direction, liste) -> list:
        new_coord = (case_init.coordonnees[0]+direction[0],
                     case_init.coordonnees[1]+direction[1])
        while(
              (test_in_grid := self.grille.is_in_grid(new_coord)) and
              self.grille.cases[new_coord].couleur == self.joueur_non_actif.couleur
             ):
                liste.append(new_coord)
                new_coord = (new_coord[0]+direction[0],
                             new_coord[1]+direction[1])
        if test_in_grid:
            if self.grille.cases[new_coord].couleur == self.joueur_actif.couleur:
                return liste
        return []

    def changer_actif(self) -> None:
        self.joueur_actif, self.joueur_non_actif = self.joueur_non_actif, self.joueur_actif
        return

    def verif_coup_jouable(self, coord): 
        return self.grille.is_in_grid(coord) and (coord in self.grille.coupsPossibles.keys())

    def jouer(self, coord):
        if self.verif_coup_jouable(coord):
            self.grille.cases[coord].couleur = self.joueur_actif.couleur
            self.grille.pions.append(coord)
            self.grille.cases_dispo.remove(coord)
            
            for direction in self.dico_directions.values():
                new_coord = (coord[0]+direction[0],
                             coord[1]+direction[1])
                if self.grille.is_in_grid(new_coord) and self.grille.cases[new_coord].couleur == 'transparent':
                    self.grille.cases_dispo.append(new_coord)

            for coord_swap in self.grille.coupsPossibles[coord]:
                self.grille.cases[coord_swap].swapCouleur()

            del self.grille.coupsPossibles[coord]
            
    def update_cases_dispo(self):
        self.grille.cases_dispo.clear()
        for case_coord in self.grille.pions:
            for direction in self.dico_directions.values():
                new_coord = (case_coord[0]+direction[0],
                             case_coord[1]+direction[1])
                if (
                    self.grille.is_in_grid(new_coord) and
                    self.grille.cases[new_coord].couleur in ('transparent', 'jouable') and
                    new_coord not in self.grille.cases_dispo
                    ):
                        self.grille.cases_dispo.append(new_coord)

