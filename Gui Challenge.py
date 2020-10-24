

import os
from tkinter import *
import tkinter as tk
import tkinter.filedialog

class MainWindow(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.title("Check files")
        loadGUI(self)

def loadGUI(self):
    btnBrowse1 = Button(text = "Browse...", command = lambda: browseDirectory(self, self.text1), height = 1, width = 15)
    btnBrowse1.grid(row = 0, column  =0, padx = (20, 0), pady = (55,0))
    btnBrowse2 = Button(text = "Browse...", command = lambda: browseDirectory(self, self.text2), height = 1, width = 15)
    btnBrowse2.grid(row = 1, column  =0, padx = (20, 0), pady = (20,0))
    btnCheck = Button(text = "Check for files...", height = 3, width = 15)
    btnCheck.grid(row = 2, column  =0, padx = (20, 0), pady = (20,20))
    btnClose = Button(text = "Close Program", height = 3, width = 15)
    btnClose.grid(row = 2, column  = 1, padx = (0, 20), pady = (20,20), sticky = E)

    self.text1 = Entry(width = 45)
    self.text1.grid(row = 0, column = 1, padx = (10, 20), pady = (55,0))
    self.text2 = Entry(width = 45)
    self.text2.grid(row = 1, column = 1, padx = (10, 20), pady = (20,0))

##def browseDirectory1(self):
##    self.text1.delete(0, END)
##    self.text1.insert(0, tk.filedialog.askdirectory())
##
##def browseDirectory1(self):
##    self.text1.delete(0, END)
##    self.text1.insert(0, tk.filedialog.askdirectory())

def browseDirectory(self, textbox):
    textbox.delete(0, END)
    textbox.insert(0, tk.filedialog.askdirectory())


root = Tk()
app = MainWindow(root)
root.mainloop()
