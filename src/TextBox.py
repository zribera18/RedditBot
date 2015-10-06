# __author__ = 'Zach'
#
# from tkinter import *
# class scrollTxtArea:
# def __init__(self,root):
#         frame=Frame(root)
#         frame.pack()
#         self.textPad(frame)
#         return
#
#     def textPad(self,frame):
#         #add a frame and put a text area into it
#         textPad=Frame(frame)
#         self.text=Text(textPad,height=50,width=90)
#
#         # add a vertical scroll bar to the text area
#         scroll=Scrollbar(textPad)
#         self.text.configure(yscrollcommand=scroll.set)
#
#         #pack everything
#         self.text.pack(side=LEFT)
#         scroll.pack(side=RIGHT,fill=Y)
#         textPad.pack(side=TOP)
#         return
# def main():
#     root = Tk()
#     foo=scrollTxtArea(root)
#     root.title('TextPad With a Vertical Scroll Bar')
#     root.mainloop()
# main()

from Tkinter import *

root = Tk()
T = Text(root, height=10, width=70)
T.pack()
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(END, quote)
mainloop()