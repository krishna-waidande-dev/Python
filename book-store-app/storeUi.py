#To create a executable file of this run below commands:
# 1. Install pyinstaller using: pip install pyinstaller
# 2. To create executable: pypinstaller -w -F storeUi.py

from tkinter import *
import storeBackend

#This logic is written for selecting any element from list.
def get_selected_row(event):
    global selected_item
    index = outputList.curselection()[0]
    selected_item = outputList.get(index)

    #Logic to add selected tuple to textbox.
    titleTxt.delete(0, END)
    titleTxt.insert(END, selected_item[1])

    authorTxt.delete(0, END)
    authorTxt.insert(END, selected_item[2])

    yearTxt.delete(0, END)
    yearTxt.insert(END, selected_item[3])

    isbnTxt.delete(0, END)
    isbnTxt.insert(END, selected_item[4])

#END is special index.
def view_command():
    outputList.delete(0, END)
    for row in storeBackend.viewAll():
        outputList.insert(END, row)

def search_command():
    outputList.delete(0, END)
    for row in storeBackend.searchEntry(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get()):
        outputList.insert(END, row)

def add_command():
    storeBackend.addEntry(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
    outputList.delete(0, END)
    outputList.insert(END, (titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get()))

def delete_command():
    storeBackend.deleteEntry(selected_item[0])

def update_command():
    storeBackend.updateEntry(selected_item[0], titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
    
#Main Window.
window = Tk()

#Title to window.
window.wm_title("Book Store")

#Labels
title = Label(window, text="Title")
title.grid(row=0, column=0)

author = Label(window, text="Author")
author.grid(row=0, column=2)

year = Label(window, text="Year")
year.grid(row=1, column=0)

isbn = Label(window, text="ISBN")
isbn.grid(row=1, column=2)

#Text Fields
titleValue = StringVar()
titleTxt = Entry(window, textvariable=titleValue)
titleTxt.grid(row=0, column=1)

authorValue = StringVar()
authorTxt = Entry(window, textvariable=authorValue)
authorTxt.grid(row=0 , column=3)

yearValue = StringVar()
yearTxt = Entry(window, textvariable=yearValue)
yearTxt.grid(row=1, column=1)

isbnValue = StringVar()
isbnTxt = Entry(window, textvariable=isbnValue)
isbnTxt.grid(row=1, column=3)

#ListBox
outputList = Listbox(window, height=6, width=35)
outputList.grid(row=3,column=0, rowspan=6, columnspan=2)

#ScrollBar
scrollBar = Scrollbar(window)
scrollBar.grid(row=3,column=2, rowspan=6)

#Attaching scrollbar to List.
outputList.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=outputList.yview)

outputList.bind('<<ListboxSelect>>', get_selected_row)

#Buttons
viewAllBtn = Button(window, text="View All", width=12, command=view_command)
viewAllBtn.grid(row=2, column=3)

searchEntryBtn = Button(window, text="Search Entry", width=12, command=search_command)
searchEntryBtn.grid(row=3, column=3)

addEntryBtn = Button(window, text="Add Entry", width=12, command=add_command)
addEntryBtn.grid(row=4, column=3)

updateEntryBtn = Button(window, text="Update Selected", width=12, command=update_command)
updateEntryBtn.grid(row=5, column=3)

deleteEntryBtn = Button(window, text="Delete Selected", width=12, command=delete_command)
deleteEntryBtn.grid(row=6, column=3)

closeBtn = Button(window, text="Close", width=12, command=window.destroy)
closeBtn.grid(row=7, column=3)

window.mainloop()