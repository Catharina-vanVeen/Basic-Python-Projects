#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

import studentTracking_gui as gui
import studentTracking_main as main

def windowCenter(window, w, h):
    screenW = window.root.winfo_screenwidth()
    screenH = window.root.winfo_screenheight()
    x = int(screenW/2 - w/2)
    y = int(screenH/2 - h/2)
    return "{}x{}+{}+{}".format(w, h, x, y)

def createDB():
    conn = sqlite3.connect("db_students.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tbl_students( \
            students_id INTEGER PRIMARY KEY AUTOINCREMENT, \
            students_fname TEXT, \
            students_lname TEXT, \
            students_phone TEXT, \
            students_email TEXT, \
            students_course \
            );")
        conn.commit()
    conn.close()

def showList(window):
    window.lst_list.delete(0, END)
    conn = sqlite3.connect("db_students.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_students ORDER BY students_lname COLLATE NOCASE, students_fname COLLATE NOCASE, students_course COLLATE NOCASE")
        studentList = cursor.fetchall()
        print(len(studentList))
        for student in studentList:
            fullname = "{}, {}".format(student[2], student[1])[:24]
            window.lst_list.insert(END, "{:03d} {:25} {}".format(student[0], fullname, student[5]))


def add(window):
    print("Add is running")
    studentID = window.txt_id.get().strip()
    fname = window.txt_fname.get().strip().title()
    lname = window.txt_lname.get().strip()
    phone = window.txt_phone.get()
    email = window.txt_email.get()
    course = window.txt_course.get()
    if studentID != "":
        confirm = messagebox.askokcancel("Student id provided", "The student ID is assigned by the database. The ID you provided will be ignored. If you wish to update an existing student, please click 'Update'. \n\nDo you wish to continue with adding this student?'")
        if not confirm:
            return
        else:
            window.txt_id.delete(0, END)
    if fname == "" or lname == "":
        messagebox.showerror("No name provided", "Please provide the first and last name of the student")
        return
    if phone == "" and email == "":
        messagebox.showerror("No contact method provided", "Please provide at least one method to contact the student")
        return
    if phone == "" or email == "":
        confirm = messagebox.askokcancel("No phone or email", "You have provided only on e method to contact the student.\n\nAre you sure you want to continue?")
        if not confirm:
            return
    if course == "":
        confirm = messagebox.askokcancel("No course provided", "You have not provided the current course for the student.\n\nAre you sure you want to continue?")
        if not confirm:
            return
    conn = sqlite3.connect("db_students.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tbl_students \
            (students_fname, students_lname, students_phone, students_email, students_course) \
            VALUES (?, ?, ?, ?, ?);", (fname, lname, phone, email, course))
        conn.commit()
    conn.close()
    clear(window)
    messagebox.showinfo("Students Added", "The student has been added to the database.")
    showList(window)

def clear(window):
        window.txt_id.delete(0, END)
        window.txt_fname.delete(0, END)
        window.txt_lname.delete(0, END)
        window.txt_phone.delete(0, END)
        window.txt_email.delete(0, END)
        window.txt_course.delete(0, END)
        

def update(window):
    print("Update is running")
    studentID = window.txt_id.get().strip()
    fname = window.txt_fname.get().strip().title()
    lname = window.txt_lname.get().strip()
    phone = window.txt_phone.get()
    email = window.txt_email.get()
    course = window.txt_course.get()
    if studentID == "" or fname == "" or lname == "":
        messagebox.showerror("No id or name provided", "Please provide the student id and the first and last name of the student")
        return
    if phone == "" and email == "":
        messagebox.showerror("No contact method provided", "Please provide at least one method to contact the student")
        return
    if phone == "" or email == "":
        confirm = messagebox.askokcancel("No phone or email", "You have provided only on e method to contact the student.\n\nAre you sure you want to continue?")
        if not confirm:
            return
    if course == "":
        confirm = messagebox.askokcancel("No course provided", "You have not provided the current course for the student.\n\nAre you sure you want to continue?")
        if not confirm:
            return

    conn = sqlite3.connect("db_students.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_students WHERE students_id = {}".format(studentID))
        studentInfo = cursor.fetchone()
        if fname != studentInfo[1] or lname != studentInfo[2]:
            confirm = messagebox.askokcancel("Confirm name update", "Did you mean to change student name from '{} {}' to '{} {}'?".format(studentInfo[1], studentInfo[2], fname, lname))
            if not confirm:
                return
        cursor.execute("UPDATE tbl_students SET students_fname = '{}', students_lname = '{}', students_phone = '{}', students_email ='{}', students_course = '{}' WHERE students_id = {}".format(fname, lname, phone, email, course, studentID))
        conn.commit()
    conn.close()
    clear(window)
    messagebox.showinfo("Students updated", "The student info has been updated in the database.")
    showList(window)
    
    
def delete(window):
    print("Delete is running")
    studentID = window.txt_id.get()
    fname = window.txt_fname.get()
    lname = window.txt_lname.get()
    phone = window.txt_phone.get()
    email = window.txt_email.get()
    course = window.txt_course.get()
    WHERE = ""
    if studentID != "":
        WHERE = "students_id = {} and ".format(studentID)
    if fname != "":
        WHERE += "students_fname = '{}' and ".format(fname)
    if lname != "":
        WHERE += "students_lname = '{}' and ".format(lname)
    if phone != "":
        WHERE += "students_phone = '{}' and ".format(phone)
    if email != "":
        WHERE += "students_email = '{}' and ".format(email)
    if course != "":
        WHERE += "students_course = '{}' and ".format(course)
    if WHERE.endswith("and "):
        WHERE = WHERE[:-4]
    if studentID =="":
        messagebox.showerror("No student ID provided", "Please select a student from the list.")
    else:
        conn = sqlite3.connect('db_students.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM tbl_students WHERE {}".format(WHERE))
            count = cursor.fetchone()[0]
            print(count)
            if count == 1:
                confirm = messagebox.askokcancel("Confirm delete", "All data pertaining to student {}, {} {} will be deleted\n\nDo you wish to continue?".format(studentID, fname, lname))
                if confirm:
                    cursor.execute("DELETE FROM tbl_students WHERE {}".format(WHERE))
                    clear(window)
            elif count == 0:
                messagebox.showerror("No records found", "No records where found with the details prvided. Select a student from the list and click delete.")
        conn.close()
        showList(window)
        
      

def filter(window):
    print("Filter is running")
    studentID = window.txt_id.get().strip()
    fname = window.txt_fname.get().strip().title()
    lname = window.txt_lname.get().strip()
    phone = window.txt_phone.get()
    email = window.txt_email.get()
    course = window.txt_course.get()
    WHERE = ""
    if fname != "":
        WHERE += "students_fname LIKE '{}' and ".format(fname)
    if lname != "":
        WHERE += "students_lname LIKE '{}' and ".format(lname)
    if phone != "":
        WHERE += "students_phone LIKE '{}' and ".format(phone)
    if email != "":
        WHERE += "students_email LIKE '{}' and ".format(email)
    if course != "":
        WHERE += "students_course LIKE '{}' and ".format(course)
    if studentID != "":
        WHERE = "students_id = {}".format(studentID)
    if WHERE.endswith("and "):
        WHERE = WHERE[:-4]
    print(WHERE)
    if WHERE == "":
        showList(window)
    else:
        window.lst_list.delete(0, END)
        conn = sqlite3.connect("db_students.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tbl_students WHERE {} ORDER BY students_lname COLLATE NOCASE".format(WHERE))
            studentList = cursor.fetchall()
            print(len(studentList))
            for student in studentList:
                fullname = "{}, {}".format(student[2], student[1])[0:24]
                window.lst_list.insert(END, "{:03d} {:25} {}".format(student[0], fullname, student[5]))
    

def select(window, event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print(value)
    studentID = int(value.split()[0])
    print(studentID)
    conn = sqlite3.connect("db_students.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_students WHERE students_id = {}".format(studentID))
        studentInfo = cursor.fetchone()
        print(studentInfo)
    conn.close()
    window.txt_id.delete(0, END)
    window.txt_id.insert(0, studentInfo[0])
    window.txt_fname.delete(0, END)
    window.txt_fname.insert(0, studentInfo[1])
    window.txt_lname.delete(0, END)
    window.txt_lname.insert(0, studentInfo[2])
    window.txt_phone.delete(0, END)
    window.txt_phone.insert(0, studentInfo[3])
    window.txt_email.delete(0, END)
    window.txt_email.insert(0, studentInfo[4])
    window.txt_course.delete(0, END)
    window.txt_course.insert(0, studentInfo[5])
        

def quit(window):
    print("Quit is running")
