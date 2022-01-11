from tkinter import *
import params
from src.classes.matrix import Matrix


# Main function --> Start the game
def main(self):
    print("--- Création de la matrice ---\n")
    matrix = Matrix(params.height, params.width)

    print("--- Création de la grille de jeu ---\n")
    self.init_grid(params.height, params.width)


# Initialization of the window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        main(self)

    # Create the grid to play
    def init_grid(self, height, width):
        print('')


# Initialization of tkinter
root = Tk()
connect4App = Window(root)

# Declaration of window (title, dimensions, etc..)
root.title("Puissance 4")
root.geometry("700x600")
root.maxsize(700, 600)
root.minsize(700, 600)

# Show window
root.mainloop()
