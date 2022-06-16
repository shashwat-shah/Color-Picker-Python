from tkinter import *
from tkinter.colorchooser import *
window=Tk()
window.title("Color Picker")
window.config(background="lightgreen")
window.geometry("330x330")
txtfield=Entry(window,bd=3,width=48,font=("sans-serif",10))
txtfield.grid(row=0,column=0)

def chooseColor():
    color=askcolor()
    print(color)
    txtfield.insert(0,color)



a=Button(text='Select Any Color',command=chooseColor,font=("Roboto",15),bg="aqua")
a.place(relx=0.5,rely=0.5,anchor=CENTER)


mainloop()