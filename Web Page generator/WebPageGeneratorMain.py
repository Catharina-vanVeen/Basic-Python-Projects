#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python version    3.8.5
#
# Author            Maria Catharina van Veen
#
# Purpose           To provide users with a tool to create
#                   or edit an html file.
#
# Tested OS         This code was written and tested to
#                   work with Windows 10.


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
        self.root.bgcolor = "#AA0000"
        self.root.config(bg = self.root.bgcolor)
        gui.loadGUI(self)


if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
