from tkinter import *

window = Tk()

def showWindow():
    window.title('ui_1.py')
    window.geometry('640x480')

def showObjects():
    def butto_1_click():
        label_1.configure(text=entry_1.get())
    
    label_1 = Label(window, text="<insert your text here>", font=("Wonderbar 2.0",10))
    butto_1 = Button(window, text="Change text", command=butto_1_click)
    entry_1 = Entry(window, width=36)

    label_1.grid(column=0,row=0)
    butto_1.grid(column=1,row=1)
    entry_1.grid(column=0,row=1)

def run():
    showWindow()
    showObjects()
    window.mainloop()

if __name__ == "__main__":
    run()