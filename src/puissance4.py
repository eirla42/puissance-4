from tkinter import *

from src.params import params
from src.classes.window import Window


# Initialization of tkinter
root = Tk()
connect4App = Window(root)

# Declaration of window (title, dimensions, etc..)
root.title('Puissance 4')
root.eval('tk::PlaceWindow . center')

# Show window
root.mainloop()
