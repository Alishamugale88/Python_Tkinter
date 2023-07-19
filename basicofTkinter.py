import tkinter

from tkinter import messagebox

#1. create window
mywin=tkinter.Tk()

#set window size
mywin.geometry("800x800")
#set title
mywin.title="ShaDow"
#pack is method of class Tk
label=tkinter.Label(mywin,text="Shadow").pack()

def fun():
  global mywin
  m=messagebox.askquestion( "Hello Python", "Hello World")
  print(m)
  if(m=='yes'):
    #destroy() will exit screen
    mywin.destroy()
  else:
    #shows msgbox 
    messagebox.showinfo("return to your screen")
    


b=tkinter.Button(mywin,text="Close",bg='brown',fg="white",command=fun).pack()

mywin.mainloop-() 
win=tkinter.Tk()

win.mainloop() 

