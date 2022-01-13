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
    # ################## print("Coordinates of the object are:", window.canvas.coords(window.discs_to_play[6]))

    print("--- Création de l'événement animant les jetons pour jouer ---\n")
    window.add_event_on_motion()

    print("--- Création de l'événement d'ajout d'un jeton sur une colonne ---\n")
    window.add_event_on_click()


# Initialization of the window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # Matrix
        self.matrix = None

        # Canvas
        self.canvas = None

        # Discs to play
        self.discs_to_play = []

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
            for disc in line:
                # Cell coordinates (top left, bottom right)
                top = disc.y * width
                bottom = top + width
                left = disc.x * width - width
                right = left + width

                # Cells
                self.canvas.create_rectangle(left, top, right, bottom, outline="gray", tags="grid")

                # Discs in the grid (smaller than a cell)
                width_coefficient = 0.13 * width
                top += width_coefficient
                bottom -= width_coefficient
                left += width_coefficient
                right -= width_coefficient

                # List of discs
                self.matrix.lines[self.matrix.lines.index(line)][line.index(disc)].shape = self.canvas.create_oval(
                    left, top, right, bottom, outline="gray"
                )

                # Discs used to play (above the grid)
                if disc.y == 1:  # Only create the disc for one line (it could be equals to 1, 2, etc.)
                    top = 0 + width_coefficient
                    bottom = width - width_coefficient

                    # List of discs to play
                    self.discs_to_play.append(
                        self.canvas.create_oval(
                            left, top, right, bottom,
                            outline="lightgray", tags="disc_to_play_" + str(disc.x),
                            activefill='yellow', activeoutline="black"
                        )
                    )

    # Event on motion
    def add_event_on_motion(self):
        self.canvas.bind("<Motion>", self.on_motion)

    # Event on click
    def add_event_on_click(self):
        self.canvas.bind("<Button-1>", self.on_click)

    # Event on motion --> When the mouse moves onto a column,
    def on_motion(self, event):
        column_coords = self.canvas.canvasy(event.x)  # Select column
        line_coords = self.cell_width / 2  # Select the line of discs to play
        sq = self.canvas.find_closest(column_coords, line_coords)[0]
        self.canvas.itemconfigure(sq, fill="red")

    # Event on click --> Add a disc on a column
    def on_click(self, event):
        column_coords = self.canvas.canvasy(event.x)  # Select column
        line_coords = self.cell_width/2  # Select the line of discs to play
        sq = self.canvas.find_closest(column_coords, line_coords)[0]
        self.canvas.itemconfigure(sq, fill="black")


# Initialization of tkinter
root = Tk()
connect4App = Window(root)

# Declaration of window (title, dimensions, etc..)
root.title("Puissance 4")
root.maxsize(params.nb_columns * params.cell_width, (params.nb_lines + 1) * params.cell_width)
root.minsize(params.nb_columns * params.cell_width, (params.nb_lines + 1) * params.cell_width)

# Show window
root.mainloop()
