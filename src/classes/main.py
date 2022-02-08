from src.classes.matrix import Matrix
from src.classes.player import Player


class Main:
    def __init__(self, window):
        self.window = window

        # Initialization menu
        self.menu()

        # Initialization connect4 game
        #self.initialization()

    # Every step to create the menu
    def menu(self):
        print("--- Création du menu avec le choix des joueurs ---\n")
        self.window.init_menu()

    # Every step to create the connect4 game
    def initialization(self, name1, name2, color1, color2):
        print("--- Création des joueurs ---\n")
        self.window.game.player1 = Player(1, name1, color1)
        self.window.game.player2 = Player(2, name2, color2)
        self.window.game.active_player = self.window.game.player1

        print("--- Création de la matrice ---\n")
        self.window.matrix = Matrix(self.window.nb_columns, self.window.nb_lines)

        print("--- Création du canvas ---\n")
        self.window.init_canvas()

        print("--- Création de la grille de jeu avec les positions des jetons ---\n")
        self.window.init_grid()

        print("--- Création de l'événement animant les jetons pour jouer ---\n")
        self.window.add_event_on_motion()

        print("--- Création de l'événement d'ajout d'un jeton sur une colonne ---\n")
        self.window.add_event_on_click_column()
