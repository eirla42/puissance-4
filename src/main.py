import tkinter as tk
import params
from src.classes.matrix import Matrix


# Initialization of the window
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        main()


# Main function --> Start the game
def main():
    print("--- Création de la matrice ---\n")
    matrix = Matrix(params.height, params.width)
    init_grid(params.height, params.width)


# Create the grid to play
def init_grid(height, width):
    print("--- Création de la grille de jeu ---\n")


root = tk.Tk()
connect4App = App(root)

# Declaration of window dimensions
connect4App.master.title("Puissance 4")
connect4App.master.geometry("700x600")
connect4App.master.maxsize(700, 600)
connect4App.master.minsize(700, 600)

connect4App.mainloop()
