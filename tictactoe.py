from tkinter import *


# class sebagai aturan dari permainan tictactoe
class GamePlay:
    def __init__(self):

        # variabel yang menyimpan nilai(x/o) pada setiap grid di papan
        # semua grid kosong di awal game
        self.check = [[0, 0, 0] for _ in range(3)] 

        # variabel yang digunakan agar grid tidak diisi dua kali
        # membuat semua grid di papan dapat diisi diawal game
        self.freeze = [[False, False, False] for _ in range(3)] 
    
    # check papan jika terdapat pemenang pada setiap giliran(xxx/ooo)
    def checkboard(self, ls_btn):

        # check baris (xxx/ooo) ?
        for i in range(3):
            if self.check[i][0] == self.check[i][1] == self.check[i][2] != 0:
                self.winner = self.check[i][0]
                ls_btn[i][0].configure(bg="red" if self.winner == "X" else "blue")
                ls_btn[i][1].configure(bg="red" if self.winner == "X" else "blue")
                ls_btn[i][2].configure(bg="red" if self.winner == "X" else "blue")

                return True

        # check kolom (xxx/ooo) >
        for i in range(3):
            if self.check[0][i] == self.check[1][i] == self.check[2][i] != 0:
                self.winner = self.check[1][i]
                ls_btn[0][i].configure(bg="red" if self.winner == "X" else "blue")
                ls_btn[1][i].configure(bg="red" if self.winner == "X" else "blue")
                ls_btn[2][i].configure(bg="red" if self.winner == "X" else "blue")

                return True

        # check diagonal kanan (xxx/ooo)  ?
        if self.check[0][0] == self.check[1][1] == self.check[2][2] != 0:
            self.winner = self.check[1][1]
            ls_btn[0][0].configure(bg="red" if self.winner == "X" else "blue")
            ls_btn[1][1].configure(bg="red" if self.winner == "X" else "blue")
            ls_btn[2][2].configure(bg="red" if self.winner == "X" else "blue")

            return True

        # check diagonal kiri (xxx/ooo) ?
        elif self.check[0][2] == self.check[1][1] == self.check[2][0] != 0:
            self.winner = self.check[1][1]
            ls_btn[0][2].configure(bg="red" if self.winner == "X" else "blue")
            ls_btn[1][1].configure(bg="red" if self.winner == "X" else "blue")
            ls_btn[2][0].configure(bg="red" if self.winner == "X" else "blue")

            return True

        return False
    
    # tidak ada pemain yang dapat mengisi grid di papan
    # hanya terjadi jika checkboard (true)
    def freezeboard(self):
        for i in range(3):
            for j in range(3):
                self.freeze[i][j] = True # semua grid tidak dapat diisi

    def resetgame(self):

        # membuat objek baru untuk class game
        # pada variabel yang sama
        self.__init__()
