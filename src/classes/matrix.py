from src.classes.disc import Disc


class Matrix:
    def __init__(self, height, width):
        # Attributes
        self.height = height
        self.width = width
        self.rows = []

        # Init the matrix
        self.init_matrix()

    # Initialize the matrix with Disc
    def init_matrix(self):
        # Lines
        for i in range(self.width, 0, -1):
            temp_line = []

            # Columns
            for j in range(self.height + 1, 0, -1):
                temp_line.append(Disc(i, j))

            # Adding lines to the matrix
            self.rows.append(temp_line)

        # Display matrix to see if it works correctly
        self.display_matrix_by_coordinates()
        self.display_matrix_by_value()

    # Display all coordinates of Discs in a Matrix
    def display_matrix_by_coordinates(self):
        print("Affichage de la matrice par coordonnées")
        for row in self.rows:
            for column in row:
                print([column.x, column.y], end=" ")
            print("")
        print("")

    # Display all value of Discs in a Matrix
    def display_matrix_by_value(self):
        print("Affichage de la matrice par valeur")
        for row in self.rows:
            for column in row:
                print(column.value, end=" ")
            print("")
        print("")
