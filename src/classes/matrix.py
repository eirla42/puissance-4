from src.classes.disc import Disc


class Matrix:
    def __init__(self, nb_columns, nb_lines):
        # Attributes
        self.nb_columns = nb_columns
        self.nb_lines = nb_lines
        self.lines = []

        # Init the matrix
        self.init_matrix()

    # Initialize the matrix with Disc
    def init_matrix(self):
        # Lines
        for i in range(self.nb_lines, 0, -1):
            temp_line = []

            # Columns
            for j in range(1, self.nb_columns + 1, 1):
                temp_line.append(Disc(j, i))

            # Adding lines to the matrix
            self.lines.append(temp_line)

        # Display matrix to see if it works correctly
        self.display_matrix_with_coordinates()
        self.display_matrix_with_value()

    # Display all coordinates of Discs in a Matrix
    def display_matrix_with_coordinates(self):
        print('Affichage de la matrice par coordonnées')
        for line in self.lines:
            for disc in line:
                print([disc.x, disc.y], end=' ')
            print('')
        print('')

    # Display all value of Discs in a Matrix
    def display_matrix_with_value(self):
        print('Affichage de la matrice par valeur')
        for line in self.lines:
            for disc in line:
                print(disc.value, end=' ')
            print('')
        print('')

    # Insert player's disc into Matrix
    def play(self, player, nb_column):
        is_disc_found = False

        # Find the lowest disc
        for line in reversed(self.lines):
            for disc in line:
                if disc == line[nb_column] and disc.value == 0:
                    disc.value = player.id
                    disc.player = player
                    is_disc_found = True
                    break

            # If a disc has changed, we don't need to go to the next line
            if is_disc_found:
                break

        self.display_matrix_with_value()

        return [self, disc] if is_disc_found else [None, None]
