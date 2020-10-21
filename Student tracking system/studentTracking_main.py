#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python version    3.8.5
#
# Author            Maria Catharina van Veen
#
# Purpose           A student tracking system application
#                   using Python with Tkinter and SQLite3,
#                   with minimum features.
#
# Tested OS         This code was written and tested to
#                   work with Windows 10.


# imports
import os
from tkinter import *
import tkinter as tk
import sqlite3

import studentTracking_func as func
import studentTracking_gui as gui

class MainWindow(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.geometry(func.windowCenter(self, 700, 450))
        self.root.title("Student Tracking App")
        self.root.config(bg = "#005500")
        func.createDB()
        gui.loadGui(self)
        



if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

