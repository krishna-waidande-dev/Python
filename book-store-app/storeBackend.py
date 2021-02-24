import sqlite3

def connect():
    conn = sqlite3.connect("books_store.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year intger, isbn integer)")
    conn.commit()
    conn.close()

def addEntry(title, author, year, isbn):
    conn = sqlite3.connect("books_store.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def viewAll():
    conn = sqlite3.connect("books_store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def searchEntry(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books_store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author=? OR year=? OR isbn = ?", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def deleteEntry(id):
    conn = sqlite3.connect("books_store.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def updateEntry(id, title, author, year, isbn):
    conn = sqlite3.connect("books_store.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()