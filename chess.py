import tkinter as tk
from functools import partial


class Chess():
    def __init__(self, master):
        self.__board = list()
        self.__frame = tk.Frame(master)
        self.__frame.configure(background="#000")

        self.img = tk.PhotoImage(
            file="img/b_pawn.png")

        for i in range(8):
            self.__board.append(list())

            for j in range(8):
                color = "#784839" if ((i + j) % 2 != 0) else "#5D3231"

                if (i + j) % 3 == 0:
                    btn = tk.Button(self.__frame, bg=color, activebackground=color, command=partial(
                        self.click, i, j), image=self.img)
                else:
                    btn = tk.Button(self.__frame, bg=color, activebackground=color, image=None,
                                    width=8, height=4, command=partial(self.click, i, j))

                btn.grid(row=i, column=j)

                self.__board[i].append(btn)

        self.__frame.pack(expand=True, anchor="c", pady=20)

    def click(self, i, j):
        self.__board[i][j]["image"] = self.img
        self.__board[i][j]["width"] = 0
        self.__board[i][j]["height"] = 0

        print(i, j)
