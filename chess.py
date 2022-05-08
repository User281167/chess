from abc import ABC, abstractmethod
import tkinter as tk


class Piece(ABC):
    @abstractmethod
    def move():
        pass


class Pawn(Piece):
    def __init__(self, is_black=False):
        pass


class Chess():
    def __init__(self, master):
        self.__board = list()
        self.__frame = tk.Frame(master)

        for i in range(8):
            self.__board.append(list())

            for j in range(8):
                color = "#784839"

                if (i + j) % 2 != 0:
                    color = "#5D3231"

                label = tk.Label(self.__frame, bg=color,
                                 width=8, height=4)
                label.grid(row=i, column=j)

                label.bind("<Button-1>", lambda x: self.click(i, j))

                self.__board[i].append(label)

        self.__frame.pack(expand=True, anchor="c", pady=20)

    def click(self, i, j):
        print(i, j)
