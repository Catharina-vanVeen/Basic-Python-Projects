#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import os
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog
import webbrowser
from tkinter import messagebox
import re

import WebPageGeneratorGui as gui
import WebPageGeneratorMain as main


def browseFilePath(window, entrybox1, entrybox2):
    filePath = tk.filedialog.askopenfilename()
    entrybox1.delete(0, END)
    entrybox1.insert(0, os.path.split(filePath)[1])
    entrybox2.delete(0, END)
    entrybox2.insert(0, os.path.split(filePath)[0])
    
def browseDirectory(window, entrybox):
    entrybox.delete(0, END)
    entrybox.insert(0, tk.filedialog.askdirectory())
    
def launch(window):
    fileName = window.header.ent_fileName.get()
    fileFolder = window.header.ent_fileFolder.get()
    
    fileHead = "<html>\n\t<body>\n"
    fileBody = window.root.txt_body.get("1.0", END)
    fileTail = "\t</body>\n</html>"

    if fileName == "" or fileFolder == "":
        messagebox.showerror("No filename or folder", "Please provide a file name and folder. You can select a file from the list, or provide a new name.")
        return
    if not os.path.isdir(fileFolder):
        messagebox.showerror("Invalid File Folder", "This folder does not exist. Please provide a valid folder")
        return
    if not fileName.endswith(".html"):
        fileName = fileName + ".html"
        window.header.ent_fileName.delete(0, END) 
        window.header.ent_fileName.insert(0, fileName)
        if not messagebox.askokcancel("File name extension", "The file name should end in '.html'. Do you accept {} as your filename?".format(fileName)):
            return
    filePath = fileFolder+os.sep+fileName
    file = open(filePath, "w")
    file.write(fileHead + fileBody + fileTail)
    file.close()
        
    webbrowser.open("file://"+filePath, new=1, autoraise=True)


def load(window):
    fileName = window.header.ent_fileName.get()
    fileFolder = window.header.ent_fileFolder.get()
    filePath = "{}\{}".format(fileFolder, fileName)
    if not os.path.isfile(filePath):
        messagebox.showerror("Invlaid file path", "The file or folder does not exist. Please provide a valid filename and folder. Use the browse button to find the file.")
        return
    file = open(filePath, "r")
    body = re.split('<body>|</body>', file.read())[1]
    window.root.txt_body.delete('1.0', END)
    window.root.txt_body.insert('1.0', body)
    file.close()
      
