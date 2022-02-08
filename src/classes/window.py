from tkinter import *

from src.classes.main import Main
from src.classes.game import Game
from src.params import params


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # Statistics of the game
        self.game = Game()

        # Matrix
        self.matrix = None

        # Canvas
        self.canvas = None

        # Discs to play
        self.discs_to_play = []

        # Dimensions
        self.nb_lines = params.NB_LINES
        self.nb_columns = params.NB_COLUMNS
        self.cell_width = params.CELL_WIDTH

        # Menu result
        self.player_1_name = None
        self.player_2_name = None
        self.player_1_color = None
        self.player_2_color = None

        # Menu texts
        self.label = None
        self.player_1_name_label = None
        self.player_2_name_label = None
        self.player_1_color_label = None
        self.player_2_color_label = None
        self.submitButton = None

        self.main = Main(self)

    # Create menu dialog
    def init_menu(self):
        font_size = self.cell_width // 5

        # Label
        self.label = Label(self.master, text="Information des joueurs", font=font_size * 2)
        self.label.pack(padx=50, pady=(10, 30))

        # Input name player 1
        self.player_1_name_label = Label(self.master, text="Nom du joueur 1", font=font_size)
        self.player_1_name_label.pack()
        self.player_1_name = Entry(self.master, width=font_size)
        self.player_1_name.pack(pady=(0, 10))

        # Select color player 1
        self.player_1_color_label = Label(self.master, text="Couleur du joueur 2 :", font=font_size)
        self.player_1_color_label.pack()
        self.player_1_color = Listbox(self.master, height=4, selectmode='single', exportselection=False)
        self.player_1_color.pack(pady=(0, 40))
        self.player_1_color.insert(0, 'yellow')
        self.player_1_color.insert(1, 'green')
        self.player_1_color.insert(2, 'blue')
        self.player_1_color.insert(3, 'white')

        # Input name player 2
        self.player_2_name_label = Label(self.master, text="Nom du joueur 2 :", font=font_size)
        self.player_2_name_label.pack()
        self.player_2_name = Entry(self.master, width=font_size)
        self.player_2_name.pack(pady=(0, 10))

        # Select color player 1
        self.player_2_color_label = Label(self.master, text="Couleur du joueur 2 :", font=font_size)
        self.player_2_color_label.pack()
        self.player_2_color = Listbox(self.master, height=4, selectmode='single', exportselection=False)
        self.player_2_color.pack(pady=(0, 40))
        self.player_2_color.insert(0, 'red')
        self.player_2_color.insert(1, 'magenta')
        self.player_2_color.insert(2, 'purple')
        self.player_2_color.insert(3, 'black')

        # Submit
        self.submitButton = Button(self.master, text="Valider", command=self.validate, font=font_size // 2)
        self.submitButton.pack(pady=(0, 10))

    # Menu validation
    def validate(self):
        self.master.maxsize(params.NB_COLUMNS * params.CELL_WIDTH, (params.NB_LINES + 1) * params.CELL_WIDTH)
        self.master.minsize(params.NB_COLUMNS * params.CELL_WIDTH, (params.NB_LINES + 1) * params.CELL_WIDTH)

        # Get all players parameters
        name1 = self.player_1_name.get() or 'Joueur 1'
        name2 = self.player_2_name.get() or 'Joueur 2'
        color1 = ",".join([self.player_1_color.get(i) for i in self.player_1_color.curselection()]) or 'yellow'
        color2 = ",".join([self.player_2_color.get(i) for i in self.player_2_color.curselection()]) or 'red'

        # Destroy menu
        self.player_1_name.destroy()
        self.player_2_name.destroy()
        self.player_1_color.destroy()
        self.player_2_color.destroy()
        self.label.destroy()
        self.player_1_name_label.destroy()
        self.player_2_name_label.destroy()
        self.player_1_color_label.destroy()
        self.player_2_color_label.destroy()
        self.submitButton.destroy()

        # Start the connect4 game
        self.main.initialization(name1, name2, color1, color2)

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

                # List of discs (from bottom to top)
                self.matrix.lines[(self.nb_lines - 1) - self.matrix.lines.index(line)][line.index(disc)].shape = \
                    self.canvas.create_oval(left, top, right, bottom, outline='gray')

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

    # Destroy event on motion
    def destroy_event_on_motion(self):
        self.canvas.unbind('<Motion>')

    # Event on click
    def add_event_on_click_column(self):
        self.canvas.bind('<Button-1>', self.on_click_column)

    # Destroy event on click
    def destroy_event_on_click_column(self):
        self.canvas.unbind('<Button-1>')

    # Event on motion --> When the mouse moves onto a column, show the player's color disc
    def on_motion(self, event):
        column_coords = self.canvas.canvasy(event.x)  # Select column
        line_coords = self.cell_width / 2  # Select the line of discs to play

        # Find the right disc and show only this one
        closest_disc = self.canvas.find_closest(column_coords, line_coords)[0]
        self.canvas.itemconfigure(closest_disc, fill=self.game.active_player.color, outline='black')
        for disc in self.discs_to_play:
            if disc != closest_disc:
                self.canvas.itemconfigure(disc, fill='seashell', outline='lightgray')

    # Event on click --> Add a disc on a column
    def on_click_column(self, event):
        column_coords = self.canvas.canvasx(event.x)  # Select column
        line_coords = self.cell_width / 2  # Select the line of discs to play

        # Find the right disc and hide it
        closest_disc = self.canvas.find_closest(column_coords, line_coords)[0]
        self.canvas.itemconfigure(closest_disc, fill='seashell', outline='lightgray')

        # Add player's disc to matrix
        matrix_and_changed_disc = self.matrix.play(self.game.active_player, int(column_coords // self.cell_width))
        temp_matrix = matrix_and_changed_disc[0]
        changed_disc = matrix_and_changed_disc[1]

        if temp_matrix:
            self.matrix = temp_matrix
            self.canvas.itemconfigure(changed_disc.shape, fill=changed_disc.player.color, outline='black')
            self.game.active_player.nb_moves += 1

            # Check if 4 discs are connected --> If a player is the winner
            if self.matrix.has_winner(self.game.active_player):
                self.game_over()
            # Switch player
            else:
                self.game.active_player = self.game.active_player.switch_player(self.game.player1, self.game.player2)

    # End of the game
    def game_over(self):
        self.game.winner = self.game.active_player
        self.game.stop_timer()
        self.game.display()
        self.game.export_csv()

        # Winning text
        game_over_text = self.game.winner.name + " gagne !"
        self.canvas.create_text(0, -100, text=game_over_text, font=('Times New Roman', self.cell_width // 2, 'bold'),
                                fill='black', tags="game_over_text", anchor='w')

        # Start the moving text and lock the game
        self.game_over_text_animation()
        self.destroy_event_on_motion()
        self.destroy_event_on_click_column()

    # Text animation with winner
    def game_over_text_animation(self):
        x1, y1, x2, y2 = self.canvas.bbox("game_over_text")
        if x2 < 0 or y1 < 0:  # Reset coordinates
            x1 = self.canvas.winfo_width()
            y1 = self.canvas.winfo_height() // 2
            self.canvas.coords("game_over_text", x1, y1)
        else:
            self.canvas.move("game_over_text", -2, 0)
        self.canvas.after(30, self.game_over_text_animation)
