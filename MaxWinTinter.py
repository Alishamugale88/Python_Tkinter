
import tkinter
from tkinter import *
from tkinter import messagebox


mywin=Tk()  #tk is class

#add title
mywin.title("Visual studio Code")

#how to maximize window size
mywin.state('zoomed')

#Add icon
mywin.iconbitmap("app.ico")

#to add menubar File Edit View Exit
menubar=Menu()
#declare menunames
File=Menu(menubar, tearoff=False)
Edit=Menu(menubar, tearoff=False)
View=Menu(menubar, tearoff=False)
Exit=Menu(menubar, tearoff=False)

#add_cascade()

menubar.add_cascade(label="File",menu=File)
menubar.add_cascade(label="Edit",menu=Edit)
menubar.add_cascade(label="View",menu=View)
menubar.add_cascade(label="Exit",menu=Exit)


mywin.config(menu=menubar)

mywin.mainloop()