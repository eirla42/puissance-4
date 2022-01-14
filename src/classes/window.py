from tkinter import *

from src.classes.main import Main
from src.params import params


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # Players
        self.active_player = None
        self.player1 = None
        self.player2 = None

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

        Main(self)

    # Create canvas
    def init_canvas(self):
        width = self.cell_width
        self.canvas = Canvas(self.master, bg='seashell',
                             height=(self.nb_lines + 1) * width, width=self.nb_columns * width)
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
                self.canvas.create_rectangle(left, top, right, bottom, outline='gray', tags='grid')

                # Discs in the grid (smaller than a cell)
                width_coefficient = 0.13 * width
                top += width_coefficient
                bottom -= width_coefficient
                left += width_coefficient
                right -= width_coefficient

                # List of discs
                self.matrix.lines[self.matrix.lines.index(line)][line.index(disc)].shape = self.canvas.create_oval(
                    left, top, right, bottom, outline='gray'
                )

                # Discs used to play (above the grid)
                if disc.y == 1:  # Only create the disc for one line (it could be equals to 1, 2, etc.)
                    top = 0 + width_coefficient
                    bottom = width - width_coefficient

                    # List of discs to play
                    self.discs_to_play.append(
                        self.canvas.create_oval(
                            left, top, right, bottom,
                            outline='lightgray', tags='disc_to_play_' + str(disc.x)
                        )
                    )

    # Event on motion
    def add_event_on_motion(self):
        self.canvas.bind('<Motion>', self.on_motion)

    # Event on click
    def add_event_on_click_column(self):
        self.canvas.bind('<Button-1>', self.on_click_column)

    # Event on motion --> When the mouse moves onto a column, show the player's color disc
    def on_motion(self, event):
        column_coords = self.canvas.canvasy(event.x)  # Select column
        line_coords = self.cell_width / 2  # Select the line of discs to play

        # Find the right disc and show only this one
        closest_disc = self.canvas.find_closest(column_coords, line_coords)[0]
        self.canvas.itemconfigure(closest_disc, fill=self.active_player.color, outline='black')
        for disc in self.discs_to_play:
            if disc != closest_disc:
                self.canvas.itemconfigure(disc, fill='seashell', outline='lightgray')

    # Event on click --> Add a disc on a column
    def on_click_column(self, event):
        column_coords = self.canvas.canvasy(event.x)  # Select column
        line_coords = self.cell_width / 2  # Select the line of discs to play

        # Find the right disc and hide it
        closest_disc = self.canvas.find_closest(column_coords, line_coords)[0]
        self.canvas.itemconfigure(closest_disc, fill='seashell', outline='lightgray')

        # Switch player
        self.active_player = self.active_player.switch_player(self.player1, self.player2)
