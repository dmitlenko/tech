from tkinter import *
from tkinter.ttk import *

class MainWindow(Tk):
     def __init__(self,size):
          Tk.__init__(self)
          self.geometry('x'.join(size))
          self._do()
     
     def _do(self):
          self.can = Canvas(self,width=300,height=300)
          self.can.pack()

if __name__ == "__main__":
     w = MainWindow(['300','300'])