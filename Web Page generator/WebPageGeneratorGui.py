

import os
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import WebPageGeneratorMain as main
import WebPageGeneratorFunc as func



def loadGUI(window):

    # HEADER
    window.root.lbl_header = Label(window.root, text="Web Page Generator", bg=window.root.bgcolor, fg = "white", font = ("Courier", 40))
    window.root.lbl_header.grid(row=0, column=0, padx = 0, pady = (25,0))
    window.header = Frame(window.root, bg=window.root.bgcolor)
    window.header.grid(row=1, column=0, padx = 0, pady = (10,10))
    
    # File Name
    window.header.lbl_fileName = Label(window.header, text="File name: ", bg=window.root.bgcolor, fg = "white")
    window.header.lbl_fileName.grid(row=0, column=0, padx = (20, 10), pady = (0,10), sticky=E)
    window.header.ent_fileName = Entry(window.header, text = "", width = 35)
    window.header.ent_fileName.grid(row=0, column=1, padx = (0, 10), pady = (0,10))
    window.header.btn_fileName = Button(window.header, text = "Browse..", command = lambda: func.browseFilePath(window, window.header.ent_fileName, window.header.ent_fileFolder), fg = window.root.bgcolor)
    window.header.btn_fileName.grid(row=0, column=2, padx = (0, 0), pady = (0,10))

    # File Folder
    window.header.lbl_fileFolder = Label(window.header, text="Folder: ", bg=window.root.bgcolor, fg = "white")
    window.header.lbl_fileFolder.grid(row=1, column=0, padx = (20, 10), pady = (0,10), sticky=E)
    window.header.ent_fileFolder = Entry(window.header, text = "", width = 35)
    window.header.ent_fileFolder.grid(row=1, column=1, padx = (0, 10), pady = (0,10))
    window.header.btn_fileFolder = Button(window.header, text = "Browse..", command = lambda: func.browseDirectory(window, window.header.ent_fileFolder), fg = window.root.bgcolor)
    window.header.btn_fileFolder.grid(row=1, column=2, padx = (0, 0), pady = (0,10))

    # Launch and Load Buttons
    window.header.btn_Launch = Button(window.header, text = "Save & Launch", command = lambda: func.launch(window), fg = window.root.bgcolor, height = 2, width = 20)
    window.header.btn_Launch.grid(row=0, column=3, rowspan=2, padx = (40, 0), pady = (0,10))
    window.header.btn_Load = Button(window.header, text = "Load file", command = lambda: func.load(window), fg = window.root.bgcolor, height = 2, width = 20)
    window.header.btn_Load.grid(row=0, column=4, rowspan=2, padx = (20, 20), pady = (0,10))
    # END HEADER
    
    # BODY
    window.root.txt_body = ScrolledText(window.root)
    window.root.txt_body.grid(row=2, column=0, columnspan = 1, padx = (20, 20), pady = (0, 20), sticky=N+E+S+W)

    
