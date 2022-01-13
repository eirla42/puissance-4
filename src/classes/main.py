from src.classes.matrix import Matrix


class Main:
    def __init__(self, window):
        print("--- Création de la matrice ---\n")
        window.matrix = Matrix(window.nb_columns, window.nb_lines)

        print("--- Création du canvas ---\n")
        window.init_canvas()

        print("--- Création de la grille de jeu avec les positions des jetons ---\n")
        window.init_grid()
        # ################## print("Coordinates of the object are:", window.canvas.coords(window.discs_to_play[6]))

        print("--- Création de l'événement animant les jetons pour jouer ---\n")
        window.add_event_on_motion()

        print("--- Création de l'événement d'ajout d'un jeton sur une colonne ---\n")
        window.add_event_on_click()
