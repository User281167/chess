import tkinter as tk
from functools import partial


class Chess():
    def __init__(self, master):
        self.__board = list()
        self.__frame = tk.Frame(master)

        for i in range(8):
            self.__board.append(list())

            for j in range(8):
                color = "#784839" if ((i + j) % 2 != 0) else "#5D3231"

                btn = tk.Button(self.__frame, bg=color, activebackground=color,
                                width=8, height=4, command=partial(self.click, i, j))

                btn.grid(row=i, column=j)

                self.__board[i].append(btn)

        self.__frame.pack(expand=True, anchor="c", pady=20)

    def click(self, i, j):
        print(i, j)
