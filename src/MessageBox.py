__author__ = 'Zach'

from Tkinter import *


root = Tk()

tkinter.messagebox.showinfo("Window Title", "monkeys")
answer = tkinter.messagebox.askquestion("Question 1", "Do you like poop")

if answer == 'yes':
    print(":)")

root.mainloop()