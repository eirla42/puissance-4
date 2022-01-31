# Contains statistics about the game witch are going to be exported in CSV
class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.active_player = None
        self.winner = None
        self.time = None

    # Display all statistics
    def display(self):
        print('--- Statistiques de fin de partie ---\n')

        print('Player 1 : ', end='')
        self.player1.display()

        print('Player 2 : ', end='')
        self.player2.display()

        print('Winner : ', end='')
        self.winner.display()

        print('Time : ', self.time)
