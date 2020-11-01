import shutil
import os
import datetime
from tkinter import *
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox

import FileCopierMain as main
import FileCopierFunc as func
import FileCopierGui as gui


def browseDirectory(window, entry):
    entry.delete(0, END)
    entry.insert(0, tk.filedialog.askdirectory())

def copyFiles(window):
    source = window.root.ent_source.get()
    destination = window.root.ent_destination.get()
    if source == "" or destination == "":
        messagebox.showerror("No Source or Destination", "Please provide a folder for the source and for the destination of the files .")
        return
    if not os.path.isdir(source):
        messagebox.showerror("Invalid Source Folder", "The source folder does not exist. Please provide a valid folder")
        return
    if not os.path.isdir(destination):
        messagebox.showerror("Invalid Destination Folder", "The destination folder does not exist. Please provide a valid folder")
        return
    files = os.listdir(source)
    count = 0
    for i in files:
        filepath = os.path.join(source, i)
        time_modified = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
        if i.endswith(".txt") and datetime.datetime.now() - time_modified <= datetime.timedelta(hours=24):
            shutil.copy2(filepath, destination)
            count += 1
    print(count)
    messagebox.showinfo("Files Copied", "{} files were copied".format(count))
