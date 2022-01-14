from tkinter import *

from src.params import params
from src.classes.window import Window


# Initialization of tkinter
root = Tk()
connect4App = Window(root)

# Declaration of window (title, dimensions, etc..)
root.title('Puissance 4')
root.eval('tk::PlaceWindow . center')
root.maxsize(params.NB_COLUMNS * params.CELL_WIDTH, (params.NB_LINES + 1) * params.CELL_WIDTH)
root.minsize(params.NB_COLUMNS * params.CELL_WIDTH, (params.NB_LINES + 1) * params.CELL_WIDTH)

# Show window
root.mainloop()
