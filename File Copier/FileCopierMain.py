import shutil
import os
import datetime
from tkinter import *
import tkinter as tk


import FileCopierMain as main
import FileCopierFunc as func
import FileCopierGui as gui


class MainWindow(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.title = "File mover"
        self.root.bgcolor = "#000055"
        self.root.config(bg = self.root.bgcolor)
        gui.loadGUI(self)










if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()











