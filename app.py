from tkinter import *
from tictactoe import GamePlay

# event untuk tombol pada papan tictactoe
def play(row, col):

    # variabel yang digunakan sebagai (x/o) dianggap sebagai pemain
    global player

    # kondisi dimana pemain adalah x
    # membuat tombol berubah menjadi x
    # akan dilakukan pengecekan apakah tombol pernah dipencet atau tidak
    # ketika tombol dipencet dicek apakah sudah ada pemenang
    if player == 'X' and not game.freeze[row][col]:
        game.check[row][col] = "X"
        button_list[row][col].configure(text="X")
        player = 'O'

        # tombol tidak akan bisa dipencet lagi
        game.freeze[row][col] = True

        # dicek apakah sudah ada yang menang (xxx/ooo)
        if game.checkboard(button_list):

            # membuat papan tictactoe tidak dapat dipencet lagi
            game.freezeboard()

    elif player == "O" and not game.freeze[row][col]:
        game.check[row][col] = "O"
        button_list[row][col].configure(text='O')
        player = 'X'
        game.freeze[row][col] = True

        if game.checkboard(button_list):
            game.freezeboard()

# reset game
def reset():
    for i in range(3):
        for j in range(3):
            # semua tombol di papan menjadi putih dan kosong
            button_list[i][j].configure(bg="white", text=" ")
    game.resetgame()

    



game = GamePlay()
window = Tk()
player = 'X'
button_list = []
button_reset = Button(window, text="reset", width=40, pady=25, command=reset)


for i in range(3):
    button1 = Button(window, bg="white", padx=40, pady=40, text=" "
                     , command= lambda r=i,c=0: play(r,c))
    button2 = Button(window, bg="white", padx=40, pady=40, text=" "
                     , command= lambda r=i,c=1: play(r,c))
    button3 = Button(window, bg="white", padx=40, pady=40, text=" "
                     , command= lambda r=i,c=2: play(r,c))

    button_list.append((button1, button2, button3))


for i in range(3):
    for j in range(3):
        button_list[i][j].grid(row=i, column=j)

button_reset.grid(row=3, column=0, columnspan=3)

window.mainloop()

