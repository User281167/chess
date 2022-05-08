import tkinter as tk
from chess import Chess


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Chess")
        self.master.geometry("600x600")
        #self.master.resizable(False, False)
        self.master.configure(background="#373737")
        self.master.iconbitmap("icon.ico")

        self.chess = Chess(master)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()
