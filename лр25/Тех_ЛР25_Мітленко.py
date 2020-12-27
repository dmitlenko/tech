from tkinter import *
from tkinter.ttk import *

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.initUI()
        self._do()

    def initUI(self):
        self.can = Canvas(self,width=262,height=422)
        self.can.pack()
    
    def _do(self):
        c = self.can
        c.create_rectangle(100,12,175,45)
        c.create_oval(95,125,183,60)
        c.create_rectangle(100,45,175,74,fill='#F0F0F0')
        c.create_line(100,45,56,74)
        c.create_line(56,74,100,74)
        c.create_rectangle(95,125,183,414)
        c.create_line(95,125,183,254)
        c.create_line(183,125,95,254)
        c.create_line(135,254,135,415)
        c.create_rectangle(95,254,183,377)
        c.create_rectangle(53,150,95,254)
        c.create_rectangle(183,150,225,254)
        c.create_line(95,125,53,150)
        c.create_line(183,125,225,150)
        c.create_line(53,254,95,300)
        c.create_line(225,254,183,300)
        c.create_line(53,414,225,414)
        c.create_line(95,377,53,414)
        c.create_line(225,414,183,377)

if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()