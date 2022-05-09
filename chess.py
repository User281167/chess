import tkinter as tk
from functools import partial
from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, chess, i, j, is_black, img_src):
        self.__chess = chess
        self.__is_black = is_black

        # board position
        self.__i = i
        self.__j = j

        self.__img = tk.PhotoImage(file=img_src)

    @property
    def is_black(self):
        return self.__is_black

    @property
    def i(self):
        return self.__i

    @property
    def j(self):
        return self.__j

    @property
    def img(self):
        return self.__img

    @abstractmethod
    def move(self):
        pass


class Pawn(Piece):
    def __init__(self, chess, i, j, is_black=False):
        img_src = "img/b_pawn.png" if is_black else "img/w_pawn.png"
        super().__init__(chess, i, j, is_black, img_src)

    def move(self):
        if self.is_black:
            print(f"Black Pawn in {self.i}, {self.j}")
        else:
            print(f"White Pawn in {self.i}, {self.j}")


class Rook(Piece):
    def __init__(self, chess, i, j, is_black=False):
        img_src = "img/b_rook.png" if is_black else "img/w_rook.png"
        super().__init__(chess, i, j, is_black, img_src)

    def move(self):
        if self.is_black:
            print(f"Black Rook in {self.i}, {self.j}")
        else:
            print(f"White Rook in {self.i}, {self.j}")


class Knight(Piece):
    def __init__(self, chess, i, j, is_black=False):
        img_src = "img/b_knight.png" if is_black else "img/w_knight.png"
        super().__init__(chess, i, j, is_black, img_src)

    def move(self):
        if self.is_black:
            print(f"Black knight in {self.i}, {self.j}")
        else:
            print(f"White knight in {self.i}, {self.j}")


class Bishop(Piece):
    def __init__(self, chess, i, j, is_black=False):
        img_src = "img/b_bishop.png" if is_black else "img/w_bishop.png"
        super().__init__(chess, i, j, is_black, img_src)

    def move(self):
        if self.is_black:
            print(f"Black Bishop in {self.i}, {self.j}")
        else:
            print(f"White Bishop in {self.i}, {self.j}")


class Queen(Piece):
    def __init__(self, chess, i, j, is_black=False):
        img_src = "img/b_queen.png" if is_black else "img/w_queen.png"
        super().__init__(chess, i, j, is_black, img_src)

    def move(self):
        if self.is_black:
            print(f"Black Queen in {self.i}, {self.j}")
        else:
            print(f"White Queen in {self.i}, {self.j}")


class King(Piece):
    def __init__(self, chess, i, j, is_black=False):
        img_src = "img/b_king.png" if is_black else "img/w_king.png"
        super().__init__(chess, i, j, is_black, img_src)

    def move(self):
        if self.is_black:
            print(f"Black King in {self.i}, {self.j}")
        else:
            print(f"White King in {self.i}, {self.j}")


class Chess():
    def __init__(self, master):
        self.__frame = tk.Frame(master)
        self.__frame.configure(background="#000")

        self.__board = list()

        self.player1 = True

        for i in range(8):
            self.__board.append(list())

            for j in range(8):
                color = "#784839" if ((i + j) % 2 != 0) else "#5D3231"
                piece = None

                # load piece
                if (i == 1 or i == 6):
                    piece = Pawn(self, i, j, i == 1)
                elif (i % 7 == 0 and j % 7 == 0):
                    piece = Rook(self, i, j, i == 0)
                elif (i % 7 == 0 and (j == 1 or j == 6)):
                    piece = Knight(self, i, j, i == 0)
                elif (i % 7 == 0 and (j + 1) % 3 == 0):
                    piece = Bishop(self, i, j, i == 0)
                elif (i % 7 == 0 and j == 3):
                    piece = Queen(self, i, j, i == 0)
                elif (i % 7 == 0 and j == 4):
                    piece = King(self, i, j, i == 0)

                if piece != None:
                    btn = tk.Button(self.__frame, bg=color, activebackground=color, width=60, height=60,
                                    command=partial(self.click, i, j), image=piece.img)
                else:
                    btn = tk.Button(self.__frame, bg=color, activebackground=color,
                                    width=8, height=4, command=partial(self.click, i, j))

                btn.grid(row=i, column=j)

                self.__board[i].append({"btn": btn, "piece": piece})

        self.__frame.pack(expand=True, anchor="c", pady=20)

    def click(self, i, j):
        btn = self.__board[i][j]["btn"]
        piece = self.__board[i][j]["piece"]

        if piece != None and ((self.player1 and not piece.is_black) or (not self.player1 and piece.is_black)):
            piece.move()
            self.player1 = not self.player1
