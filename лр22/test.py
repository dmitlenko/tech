from tkinter import *
from tkinter.ttk import *

root = Tk()

fr1 = LabelFrame(root,text='l1',width=340,height=340)
fr2 = LabelFrame(fr1,text='l2',width=300,height=300)

fr1.pack(side=LEFT)
fr2.pack(side=RIGHT)

root.mainloop()