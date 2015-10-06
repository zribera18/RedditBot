__author__ = 'Zach'

from Tkinter import *


def doNothing():
    print("okay i will not")


root = Tk()

# ***** Menu ******
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New File..", command=doNothing)
subMenu.add_command(label="New poop", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ***** Toolbar ******
toolBar = Frame(root, bg="blue")
insertButt = Button(toolBar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolBar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)
toolBar.pack(side=TOP, fill=X)

# *****Statusbar ******
status = Label(root, text="Preparing to do nothing fool", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
