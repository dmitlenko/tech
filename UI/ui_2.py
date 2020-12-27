from tkinter import *
from tkinter.ttk import *

root = Tk()

def learnTemp():
     if r_var.get() == 0:
           label1['text'] ="текст1"
     elif r_var.get() == 1:
          label1['text'] = "текст2"
     elif r_var.get() == 2:
          label1['text'] = "текст3" 
     elif r_var.get() == 3:
          label1['text'] = "текст4"

r_var = IntVar()
r_var.set(0)
r1 = Radiobutton(root,text="Флегматик", variable=r_var, value=0)
r2 = Radiobutton(root,text="Меланхолік", variable=r_var, value=1)
r3 = Radiobutton(root,text="Холерик", variable=r_var, value=2)
r4 = Radiobutton(root,text="Сангвінік", variable=r_var, value=3)
button = Button(root,command=learnTemp)
label1 = Label()
r1.pack()
r2.pack()
r3.pack()
r4.pack()
label1.pack()
button.pack()

root.mainloop()