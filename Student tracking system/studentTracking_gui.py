#!/usr/bin/python
# -*- coding: utf-8 -*-# imports
import os
from tkinter import *
import tkinter as tk
import sqlite3

import studentTracking_func as func
import studentTracking_main as main


def loadGui(window):

    # Labels
    window.lbl_id = tk.Label(window.root, text = "Student ID:", bg = "#005500", fg = "white")
    window.lbl_id.grid(row = 0, column = 0, rowspan = 1, columnspan = 1, padx = (20, 0), pady = (10, 0), sticky = W)
    window.lbl_fname = tk.Label(window.root, text = "First Name:", bg = "#005500", fg = "white")
    window.lbl_fname.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, padx = (20, 0), pady = (10, 0), sticky = W)
    window.lbl_lname = tk.Label(window.root, text = "Last Name:", bg = "#005500", fg = "white")
    window.lbl_lname.grid(row = 4, column = 0, rowspan = 1, columnspan = 1, padx = (20, 0), pady = (10, 0), sticky = W)
    window.lbl_phone = tk.Label(window.root, text = "Phone Number:", bg = "#005500", fg = "white")
    window.lbl_phone.grid(row = 6, column = 0, rowspan = 1, columnspan = 1, padx = (20, 0), pady = (10, 0), sticky = W)
    window.lbl_email = tk.Label(window.root, text = "Email Address:", bg = "#005500", fg = "white")
    window.lbl_email.grid(row = 8, column = 0, rowspan = 1, columnspan = 1, padx = (20, 0), pady = (10, 0), sticky = W)
    window.lbl_course = tk.Label(window.root, text = "Current Course:", bg = "#005500", fg = "white")
    window.lbl_course.grid(row = 10, column = 0, rowspan = 1, columnspan = 1, padx = (20, 0), pady = (10, 0), sticky = W)

    # Text(Entry) boxes
    window.txt_id = tk.Entry(window.root)
    window.txt_id.grid(row = 1, column = 0, rowspan = 1, columnspan = 2, padx = (20, 0), pady = (5, 0), sticky = W+E)
    window.txt_fname = tk.Entry(window.root)
    window.txt_fname.grid(row = 3, column = 0, rowspan = 1, columnspan = 2, padx = (20, 0), pady = (5, 0), sticky = W+E)
    window.txt_lname = tk.Entry(window.root)
    window.txt_lname.grid(row = 5, column = 0, rowspan = 1, columnspan = 2, padx = (20, 0), pady = (5, 0), sticky = W+E)
    window.txt_phone = tk.Entry(window.root)
    window.txt_phone.grid(row = 7, column = 0, rowspan = 1, columnspan = 2, padx = (20, 0), pady = (5, 0), sticky = W+E)
    window.txt_email = tk.Entry(window.root)
    window.txt_email.grid(row = 9, column = 0, rowspan = 1, columnspan = 2, padx = (20, 0), pady = (5, 0), sticky = W+E)
    window.txt_course = tk.Entry(window.root)
    window.txt_course.grid(row = 11, column = 0, rowspan = 1, columnspan = 2, padx = (20, 0), pady = (5, 0), sticky = W+E)

    # Listbox
    window.lbl_list = tk.Label(window.root, text = "Students:", bg = "#005500", fg = "white")
    window.lbl_list.grid(row = 0, column =2, rowspan = 1, columnspan = 1, padx = (20, 0), pady = (10, 0), sticky = W)
    window.lst_list = tk.Listbox(window.root, selectmode = tk.SINGLE ,  font="Courier 8", fg = "#005500")
    window.lst_list.grid(row = 1, column = 2, rowspan = 11, columnspan = 3, padx = (20, 0), pady = (5, 0), sticky = N+E+S+W)
    window.lst_list.bind("<<ListboxSelect>>", lambda event: func.select(window, event))
    
    # Buttons
    window.btn_add = tk.Button(window.root, width = 12, height = 2, text = "Add", fg = "#005500", command = lambda: func.add(window))
    window.btn_add.grid(row=12,column=0,padx=(20,0),pady=(45,10),sticky=W)
    window.btn_update = tk.Button(window.root, width = 12, height = 2, text = "Update", fg = "#005500", command = lambda: func.update(window))
    window.btn_update.grid(row=12,column=1,padx=(20,0),pady=(45,10),sticky=W)
    window.btn_delete = tk.Button(window.root, width = 12, height = 2, text = "Delete", fg = "#005500", command = lambda: func.delete(window))
    window.btn_delete.grid(row=12,column=2,padx=(20,0),pady=(45,10),sticky=W)
    window.btn_filter = tk.Button(window.root, width = 12, height = 2, text = "Filter", fg = "#005500", command = lambda: func.filter(window))
    window.btn_filter.grid(row=12,column=3,padx=(20,0),pady=(45,10),sticky=W)
    window.btn_close = tk.Button(window.root, width = 12, height = 2, text = "Close", fg = "#005500", command = lambda: func.quit(window))
    window.btn_close.grid(row=12,column=4,padx=(20,0),pady=(45,10),sticky=W)
    
