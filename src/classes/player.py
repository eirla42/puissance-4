class Player:
    def __init__(self, player_id, name, color):
        self.id = player_id
        self.name = name
        self.color = color
        self.nb_moves = 0

    # Switch the player who is playing
    def switch_player(self, player1, player2):
        if self == player1:
            return player2
        else:
            return player1

    # Display player
    def display(self):
        print(self.id, '-', self.name, '-', self.color, '-', self.nb_moves)
