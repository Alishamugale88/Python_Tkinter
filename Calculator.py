"""1.pip install pyinstaller
   2.pyinstaller --onefile --windowed .\Calculator.py
   3.(last after all code is completed )pyinstaller --onefile --windowed .\Calculator.py"""


import tkinter
from tkinter import *
from tkinter import messagebox

mywin=Tk()  #tk is class

#n1 = Entry(mywin).pack()
#n2 =Entry(mywin).pack()
mywin.geometry("600x600")
n1 = Entry(mywin)
n2 = Entry(mywin)
n1.grid(row=0,column=1)
n2.grid(row=2,column=1)

l1=Label(mywin,text="Enter number  : ")
l1.grid(row=0,column=0)

l2=Label(mywin,text="Enter number  : ")
l2.grid(row=2,column=0)

def closewin():
    mywin.destroy()

def calculate_Sum():
    #print(n1.get())
    res=float(n1.get())+float(n2.get())
    Label(mywin,text="SUM :     {}".format(res)).grid(row=6,column=0)
    #messagebox.showinfo("SUM  :   ",res)

b1=Button(mywin,text="Exit",command=closewin).grid(row=9,column=1)
b2=Button(mywin,text="SUM",command=calculate_Sum).grid(row=9)


mywin.mainloop()