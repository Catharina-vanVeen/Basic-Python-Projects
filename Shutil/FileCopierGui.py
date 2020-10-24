import shutil
import os
import datetime
from tkinter import *
import tkinter as tk


import FileCopierMain as main
import FileCopierFunc as func
import FileCopierGui as gui


def loadGUI(window):
    # Header
    window.root.lbl_header = Label(window.root, text="File Copier", bg=window.root.bgcolor, fg = "white", font = ("Courier", 40))
    window.root.lbl_header.grid(row=0, column=0, columnspan=3, padx = 0, pady = (25,0), sticky=E+W)
    
    # Source Folder
    window.root.lbl_source = Label(window.root, text="Source Folder: ", bg=window.root.bgcolor, fg = "white")
    window.root.lbl_source.grid(row=1, column=0, padx = (20, 10), pady = (0,10), sticky=E)
    window.root.ent_source = Entry(window.root, text = "", width = 35)
    window.root.ent_source.grid(row=1, column=1, padx = (0, 10), pady = (0,10))
    window.root.btn_source = Button(window.root, text = "Browse..", command = lambda: func.browseDirectory(window, window.root.ent_source), fg = window.root.bgcolor)
    window.root.btn_source.grid(row=1, column=2, padx = (0, 20), pady = (0,10))

    # Destination Folder
    window.root.lbl_destination = Label(window.root, text="Destination Folder: ", bg=window.root.bgcolor, fg = "white")
    window.root.lbl_destination.grid(row=2, column=0, padx = (20, 10), pady = (0,10), sticky=E)
    window.root.ent_destination = Entry(window.root, text = "", width = 35)
    window.root.ent_destination.grid(row=2, column=1, padx = (0, 10), pady = (0,10))
    window.root.btn_destination = Button(window.root, text = "Browse..", command = lambda: func.browseDirectory(window, window.root.ent_destination), fg = window.root.bgcolor)
    window.root.btn_destination.grid(row=2, column=2, padx = (0, 20), pady = (0,10))

    # Launch and Load Buttons
    window.root.btn_Launch = Button(window.root, text = "Copy Files", command = lambda: func.copyFiles(window), fg = window.root.bgcolor, height = 2, width = 20)
    window.root.btn_Launch.grid(row=5, column=0, rowspan=2, columnspan=3, padx = (40, 0), pady = (0,10))
    
    
