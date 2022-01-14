class Player:
    def __init__(self, player_id, name, color):
        self.id = player_id
        self.name = name
        self.color = color

    # Switch the player who is playing
    def switch_player(self, player1, player2):
        if self == player1:
            return player2
        else:
            return player1
