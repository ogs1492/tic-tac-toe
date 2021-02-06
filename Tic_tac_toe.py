from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill = BOTH, expand = 1)

def checkWin():
    checkDiagonals()
    checkRows()
    checkColumns()

def checkDiagonals():
    if board[0][0] == board[1][1] == board[2][2] != 0:
        win(board[0][0])
    if board[0][2] == board[1][1] == board[2][0] != 0:
        win(board[2][0])

def checkRows():
    if board[0][0] == board[0][1] == board[0][2] != 0:
        win(board[0][0])
    if board[1][0] == board[1][1] == board[1][2] != 0:
        win(board[1][0])
    if board[2][0] == board[2][1] == board[2][2] != 0:
        win(board[2][0])

def checkColumns():
    if board[0][0] == board[1][0] == board[2][0] != 0:
        win(board[0][0])
    if board[0][1] == board[1][1] == board[2][1] != 0:
        win(board[0][1])
    if board[0][2] == board[1][2] == board[2][2] != 0:
        win(board[0][2])

def win(player):
    if player == 1:
        global playerOneWins
        global p1counter
        print("Player One Wins")
        playerOneWins += 1
        p1counter.configure(text = playerOneWins)
    if player == 2:
        global playerTwoWins
        global p2counter
        print("Player Two Wins")
        playerTwoWins += 1
        p2counter.configure(text = playerTwoWins)
    reset()

def click(btnid, row, column):
    global turn
    if turn % 2 == 0:
        btnid.configure(image = xImage)
        turn += 1
        board[row][column] = 1
    else:
        btnid.configure(image = oImage)
        turn += 1
        board[row][column] = 2
    btnid.configure(command = NONE)
    checkWin()

def reset():
    board = [[0,0,0], [0,0,0], [0,0,0]]
    for sq in squares:
        sq.configure(image = blank)

turn = 0
root = Tk()
window = Window(root)
root.wm_title("Tic tac toe")
root.geometry("400x600")

board = [[0,0,0], [0,0,0], [0,0,0]]

playerOneWins = 0
playerTwoWins = 0

xImage = ImageTk.PhotoImage(Image.open("x.png"))
oImage = ImageTk.PhotoImage(Image.open("o.png"))
blank = ImageTk.PhotoImage(Image.open("blank.png"))

p1 = Label(root, text = "Player 1:", font = ("Helvetica", 10))
p1.place(x = 310, y = 0)

p1counter = Label(root, text = "0", font = ("Helvetica", 20))
p1counter.place(x = 340, y = 30)

p2 = Label(root, text = "Player 2:", font = ("Helvetica", 10))
p2.place(x = 310, y = 100)

p2counter = Label(root, text = "0", font = ("Helvetica", 20))
p2counter.place(x = 340, y = 130)



global oo
oo = Button(root)
oo.configure(command = lambda id = oo:  click(btnid = id, row = 0, column=0))
oo.place(x=0, y=0)

global ot
ot = Button(root)
ot.configure(command = lambda id=ot: click(btnid = id, row = 1, column=0))
ot.place(x=0, y=100)

global oh
oh = Button(root)
oh.configure(command = lambda id=oh: click(btnid = id, row = 2, column=0))
oh.place(x=0, y=200)

global to
to = Button(root)
to.configure(command = lambda id=to: click(btnid = id,  row = 0, column=1))
to.place(x=100, y=0)

global tt
tt = Button(root)
tt.configure(command = lambda id=tt: click(btnid = id, row = 1, column=1))
tt.place(x=100, y=100)

global th
th = Button(root)
th.configure(command = lambda id=th: click(btnid = id, row = 2, column=1))
th.place(x=100, y=200)

global ho
ho = Button(root)
ho.configure(command = lambda id=ho: click(btnid = id, row = 0, column=2))
ho.place(x=200, y=0)

global ht
ht = Button(root)
ht.configure(command = lambda id=ht: click(btnid = id, row = 1, column=2))
ht.place(x=200, y=100)

global hh
hh = Button(root)
hh.configure(command = lambda id=hh: click(btnid = id, row = 2, column=2))
hh.place(x=200, y=200)

squares = [oo, ot, oh, to, tt, th, ho, ht, hh]

for sq in squares:
    sq.configure(height = 100, width = 100, image = blank, relief = FLAT)

root.mainloop()