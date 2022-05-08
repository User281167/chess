import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Chess")
        self.master.geometry("600x600")
        self.master.resizable(False, False)
        self.master.configure(background="white")
        self.master.iconbitmap("icon.ico")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()
