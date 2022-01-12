from tkinter import *
import params
from src.classes.matrix import Matrix


# Main function --> Start the game
def main(window):
    print("--- Création de la matrice ---\n")
    window.matrix = Matrix(window.nb_columns, window.nb_lines)

    print("--- Création du canvas ---\n")
    window.init_canvas()

    print("--- Création de la grille de jeu avec les positions des jetons ---\n")
    window.init_grid()


# Initialization of the window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # Matrix
        self.matrix = None

        # Canvas
        self.canvas = None

        # Discs
        self.discs = None

        # Dimensions
        self.nb_lines = params.nb_lines
        self.nb_columns = params.nb_columns
        self.cell_width = params.cell_width

        main(self)

    # Create canvas
    def init_canvas(self):
        width = self.cell_width
        self.canvas = Canvas(root, bg="seashell", height=(self.nb_lines + 1) * width, width=self.nb_columns * width)
        self.canvas.pack()

    # Create the grid to play
    def init_grid(self):
        width = self.cell_width
        for line in self.matrix.lines:
            for column in line:
                # Cell coordinates (top left, bottom right)
                top = column.y * width
                bottom = top + width
                left = column.x * width - width
                right = left + width

                # Cells
                self.canvas.create_rectangle(left, top, right, bottom, outline="gray", tags="grid")

                # Discs in the grid
                width_to_add_or_remove = 0.13 * width
                top += width_to_add_or_remove
                bottom -= width_to_add_or_remove
                left += width_to_add_or_remove
                right -= width_to_add_or_remove
                self.canvas.create_oval(
                    left, top, right, bottom, outline="gray", tags="grid"
                )

                # Discs used to play (above the grid)
                if column.y == 1:
                    top = 0 + width_to_add_or_remove
                    bottom = width - width_to_add_or_remove
                    self.canvas.create_oval(
                        left, top, right, bottom,
                        outline="gray", tags="disc_to_play_" + str(column.x),
                        activefill='yellow', activeoutline="black"
                    )


# Initialization of tkinter
root = Tk()
connect4App = Window(root)

# Declaration of window (title, dimensions, etc..)
root.title("Puissance 4")
root.maxsize(params.nb_columns * params.cell_width, (params.nb_lines + 1) * params.cell_width)
root.minsize(params.nb_columns * params.cell_width, (params.nb_lines + 1) * params.cell_width)

# Show window
root.mainloop()
