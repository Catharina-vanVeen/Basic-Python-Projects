
import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

def addToTable(fname):
    conn = sqlite3.connect("test2.db")
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files (files_name) VALUES (?)", \
            (fname,))
        conn.commit
    conn.close

# CREATE TABLE
conn = sqlite3.connect("test2.db")
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        files_id INTEGER PRIMARY KEY AUTOINCREMENT,\
        files_name TEXT\
        )")
    conn.commit
conn.close

# POPULATE TABLE WITH QUALIFYINF ITEMS FROM LIST
for i in fileList:
    if i.endswith(".txt"):
        addToTable(i)

# PRINT QUALIFYING ITEMS TO CONSOLE.
# SINCE ONLY QUALIFYING ITEMS
# ARE IN TABLE NO WHERE CLAUSE IS NEEDED
conn = sqlite3.connect("test2.db")
with conn:
    cur = conn.cursor()
    cur.execute("SELECT files_name FROM tbl_files")
    list = cur.fetchall()
    for i in list:
        print(i[0])
