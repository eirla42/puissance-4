from tkinter import *
import params
from src.classes.matrix import Matrix


# Main function --> Start the game
def main(window):
    print("--- Création de la matrice ---\n")
    matrix = Matrix(window.nb_columns, window.nb_lines)

    print("--- Création du canvas ---\n")
    window.init_canvas()

    print("--- Création de la grille de jeu ---\n")
    window.init_grid()


# Initialization of the window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.canvas = None
        self.nb_lines = params.nb_lines
        self.nb_columns = params.nb_columns
        self.cell_width = params.cell_width

        main(self)

    # Create canvas
    def init_canvas(self):
        width = self.cell_width
        self.canvas = Canvas(root, bg="seashell", height=self.nb_lines * width, width=self.nb_columns * width)
        self.canvas.pack()

    # Create the grid to play
    def init_grid(self):
        print('')


# Initialization of tkinter
root = Tk()
connect4App = Window(root)

# Declaration of window (title, dimensions, etc..)
root.title("Puissance 4")
root.maxsize(params.nb_columns * params.cell_width, params.nb_lines * params.cell_width)
root.minsize(params.nb_columns * params.cell_width, params.nb_lines * params.cell_width)

# Show window
root.mainloop()
