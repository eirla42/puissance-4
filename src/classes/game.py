import time
from src.functions import convertTime


# Contains statistics about the game witch are going to be exported in CSV
class Game:
    def __init__(self):
        # Players
        self.player1 = None
        self.player2 = None
        self.active_player = None
        self.winner = None

        # Times in seconds
        self.start_time = time.time()
        self.end_time = None
        self.game_time = None

    # Calculate the time of the game, and stop the timer
    def stop_timer(self):
        self.end_time = time.time()
        self.game_time = self.end_time - self.start_time

    # Display all statistics
    def display(self):
        print('--- Statistiques de fin de partie ---\n')

        print('Player 1 : ', end='')
        self.player1.display()

        print('Player 2 : ', end='')
        self.player2.display()

        print('Winner : ', end='')
        self.winner.display()

        print('Start time : ', convertTime.seconds_to_date(self.start_time))
        print('End time : ', convertTime.seconds_to_date(self.end_time))
        print('Game time : ', convertTime.seconds_to_h_m_s(self.game_time))
