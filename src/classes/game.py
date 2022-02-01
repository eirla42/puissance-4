import time
import pandas as pd
from os.path import exists
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

    # Export statistics to a csv file
    def export_csv(self):
        data_title = [
            'player1_id', 'player1_name', 'player1_color', 'player1_nb_moves',
            'player2_id', 'player2_name', 'player2_color', 'player2_nb_moves',
            'winner_id', 'winner_name', 'winner_color', 'winner_nb_moves'
        ]
        data_to_export = {
            'player1_id': str(self.player1.id), 'player1_name': self.player1.name,
            'player1_color': self.player1.color, 'player1_nb_moves': str(self.player1.nb_moves),
            'player2_id': str(self.player2.id), 'player2_name': self.player2.name,
            'player2_color': self.player2.color, 'player2_nb_moves': str(self.player2.nb_moves),
            'winner_id': str(self.winner.id), 'winner_name': self.winner.name,
            'winner_color': self.winner.color, 'winner_nb_moves': str(self.winner.nb_moves)
        }
        dataframe = pd.DataFrame(data_to_export, columns=data_title, index='0')

        # Export statistics (and headers if the file does not exist yet)
        csv_path = './previous_games.csv'
        if exists(csv_path):
            dataframe.to_csv(csv_path, mode='a', index=False, header=False, sep=';')
        else:
            dataframe.to_csv(csv_path, mode='a', index=False, header=True, sep=';')
