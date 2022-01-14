from tkinter import *

from src.params import params
from src.classes.window import Window


# Initialization of tkinter
root = Tk()
connect4App = Window(root)

# Declaration of window (title, dimensions, etc..)
root.title('Puissance 4')
root.maxsize(params.nb_columns * params.cell_width, (params.nb_lines + 1) * params.cell_width)
root.minsize(params.nb_columns * params.cell_width, (params.nb_lines + 1) * params.cell_width)

# Show window
root.mainloop()
