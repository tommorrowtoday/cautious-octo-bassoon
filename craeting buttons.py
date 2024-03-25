from tkinter import *

root = Tk()
#for mean the button create function
def myclick():
	myLabel = Label(root, text="look i clicked my myButton")
	myLabel.pack()

myButton =Button(root, text="click here",command=myclick ,fg="green", bg="black")#, pady=50 and padx=50 it for button size"it in axis")#,state=DISABLED)IT'S FOR BUTTON CAN'T M
myButton.pack()

root.mainloop()