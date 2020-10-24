

import os
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import WebPageGeneratorGui as gui
import WebPageGeneratorFunc as func

class MainWindow(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.title("Web Page Generator")
        self.root.bgcolor = "#550000"
        self.root.config(bg = self.root.bgcolor)
        gui.loadGUI(self)






if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
