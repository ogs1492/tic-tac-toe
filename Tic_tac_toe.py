import tkinter as tk
from PIL import Image, ImageTk

# Initialize so images can load
root = tk.Tk()
turn = 0

# Class that wraps the functionality of each square
class Square(tk.Button):
    def __init__(self, game, x, y):
        self.game = game
        self.value = 0;
        super().__init__(root, bd = 0)
        super().configure(command = self.click, image = self.blankImage)
        super().place(x = x, y = y)

    def click(self):
        if self.clicked == False:
            global turn
            if turn % 2 == 0:
                self.value = 1
            else:
                self.value = 2
            self.draw();
            self.clicked = True
            turn += 1
            self.game.checkWin()
            
    def draw(self):
            if self.value == 0:
               super().configure(image = self.blankImage)
            elif self.value == 1:
               super().configure(image = self.xImage)
            elif self.value == 2:
               super().configure(image = self.oImage)        
    
    def reset(self):
        self.value = 0
        self.clicked = False
        self.draw()

    game = None
    # The images used for the squares
    blankImage = ImageTk.PhotoImage(Image.open("blank.png"))
    xImage = ImageTk.PhotoImage(Image.open("x.png"))
    oImage = ImageTk.PhotoImage(Image.open("o.png"))

    # The current state of the square. 0 = blank. 1 = X (player 1). 2 = O (player 2)
    value = 0
    clicked = False

class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.oo = Square(self, 0, 0)
        self.ot = Square(self, 0, 100)
        self.oh = Square(self, 0, 200)
        self.to = Square(self, 100, 0)
        self.tt = Square(self, 100, 100)
        self.th = Square(self, 100, 200)
        self.ho = Square(self, 200, 0)
        self.ht = Square(self, 200, 100)
        self.hh = Square(self, 200, 200)
        self.board = [[self.oo, self.ot, self.oh], [self.to, self.tt, self.th], [self.ho, self.ht, self.hh]]
        self.p1Label.place(x = 300, y = 0)
        self.p1ScoreLabel.place(x = 300, y = 30)
        self.p2Label.place(x = 300, y = 100)
        self.p2ScoreLabel.place(x = 300, y = 130)
        super().pack()

    def updateLabels(self):
        self.p1ScoreLabel.config(text = str(self.p1Score))
        self.p2ScoreLabel.config(text = str(self.p2Score))
        
    def checkColumns(self):
        for r in self.board:
            if r[0].value == r[1].value == r[2].value != 0:
                self.win = True
    
    def checkRows(self):
        for i in range(0, 3):
            if self.board[0][i].value == self.board[1][i].value == self.board[2][i].value != 0:
                self.win = True
    
    def checkDiagonals(self):
        if self.board[0][0].value == self.board[1][1].value == self.board[2][2].value != 0 or \
           self.board[2][0].value == self.board[1][1].value == self.board[0][2].value != 0:
            self.win = True

    def checkWin(self):
        global turn
        self.checkColumns()
        self.checkRows()
        self.checkDiagonals()
        if self.win == True:
            
            if turn % 2 == 1:
                self.p1Score += 1
            else:
                self.p2Score += 1
            turn = 0
            self.win = False
            self.updateLabels()
            for r in self.board:
                for c in r:
                    c.reset()

    win = False
    # Squares used for the gameboard. o = One, t = Two, h = Three
    oo = None
    ot = None
    oh = None
    to = None
    tt = None
    th = None
    ho = None
    ht = None
    hh = None
    # The gameboard as an array
    board = []
    # Player score and counters
    p1Score = 0
    p1Label = tk.Label(root, text = "Player 1:")
    p1ScoreLabel = tk.Label(root, text = "0", font = ("Arial", 25))
    p2Score = 0
    p2Label = tk.Label(root, text = "Player 2:")
    p2ScoreLabel = tk.Label(root, text = "0", font = ("Arial", 25))

    
# Actual initalization of the game
root.geometry("400x300")
root.wm_title("Tic-tac-toe")
global game
game = Game(master=root)
game.mainloop()
