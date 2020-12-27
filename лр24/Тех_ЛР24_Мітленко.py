from tkinter import *
from tkinter.ttk import *
from math import *
from json import dumps
from datetime import datetime

class ButtonSlider(Frame):
    def __init__(self,master,inc_dec,value,max_,min_,label='',onchange=None):
        Frame.__init__(self,master)
        self.inc_dec = inc_dec
        self.value = value
        self.labelText = label
        self.min = min_
        self.max = max_
        self.var = StringVar()
        self._onchange = onchange
        self.var.set(value)
        self.initUI()
        

    def updateView(self):
        self.entry.delete(0,END)
        self.entry.insert(0,str(round(self.value,3)))

    def inc(self,event):
        if (self.value + self.inc_dec) <= self.max:
            self.value += self.inc_dec
            self.updateView()
            self._onchange(self)

    def dec(self,event):
        if (self.value - self.inc_dec) >= self.min:
            self.value -= self.inc_dec
            self.updateView()
            self._onchange(self)

    def var_change(self,*args):
        try:
            if isinstance(self.value,float):
                val = float(self.var.get())
            else:
                val = int(self.var.get())
            if self.min <= val <= self.max:
                self.value = val
                self._onchange(self)
                self.updateView()
        except: 
            pass

    def initUI(self):
        self.but_min = b1 = Button(self,text="-" + str(round(self.inc_dec,2)),width=7)
        self.but_add = b2 = Button(self,text="+" + str(round(self.inc_dec,2)),width=7)
        self.entry   = e1 = Entry(self,width=12,textvariable=self.var)
        self.label   = l1 = Label(self,text=self.labelText + ':',width=12)
        v1 = self.var

        b1.bind('<Button-1>', self.dec)
        b2.bind('<Button-1>', self.inc)
        v1.trace_add('write', self.var_change)

        l1.grid(column=1,row=0)
        b1.grid(column=0,row=1)
        e1.grid(column=1,row=1)
        b2.grid(column=2,row=1)    

        self.updateView()

    def __str__(self):
        return '%f'%self.value

class TextScroll(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.txt = Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        scrollb = Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

class Settings(Toplevel):
    def __init__(self,master,callback):
        Toplevel.__init__(self)
        def apply():
            self.func_color = drop3_var.get()
            self.grid_color = drop1_var.get()
            self.lines_color= drop2_var.get()
            self.destroy()
            callback(self)

        def updateShow(*args):
            try:
                show1.config(background=drop1_var.get())
                show2.config(background=drop2_var.get())
                show3.config(background=drop3_var.get())
            except: pass

        self.resizable(False, False)
        self.title('Налаштування')
        self.geometry('290x190')
        master.eval(f'tk::PlaceWindow {str(self)} center')

        drop1_var = StringVar()
        drop2_var = StringVar()
        drop3_var = StringVar()

        drop1_var.trace_add('write',updateShow)
        drop2_var.trace_add('write',updateShow)
        drop3_var.trace_add('write',updateShow)

        drop_width = 8

        drop1_var.set(master.grid_color)
        drop2_var.set(master.lines_color)
        drop3_var.set(master.func_color)

        colors = lambda f,df: [f,df,"#ed254e","#69dc9e","#ca7df9","#250001","#335c67"]

        drop1 = OptionMenu(self,drop1_var,*colors(master.grid_color,master.default_grid_color))
        drop2 = OptionMenu(self,drop2_var,*colors(master.lines_color,master.default_lines_color))
        drop3 = OptionMenu(self,drop3_var,*colors(master.func_color,master.default_lines_color))
        chec1 = Checkbutton(self,text='Дод. інфо.',onvalue=1,offvalue=0,variable=master.enableDataDrawing)
        chec2 = Checkbutton(self,text='Темна тема',onvalue=1,offvalue=0,variable=master.invertCanvas)
        show1 = Label(self,text='',width=drop_width)
        show2 = Label(self,text='',width=drop_width)
        show3 = Label(self,text='',width=drop_width)
        apply = Button(self,text='Примінити',command=apply)

        drop1.config(width=drop_width)
        drop2.config(width=drop_width)
        drop3.config(width=drop_width)

        Label(self,text='Колір сітки:').grid(column=0,row=0,sticky="ew",padx=10,pady=10)
        drop1.grid(column=1,row=0,sticky="ew",padx=10,pady=10)
        show1.grid(column=2,row=0,sticky="ew",padx=10,pady=10)
        Label(self,text='Колір ліній:').grid(column=0,row=1,sticky="ew",padx=10,pady=10)
        drop2.grid(column=1,row=1,sticky="ew",padx=10,pady=10)
        show2.grid(column=2,row=1,sticky="ew",padx=10,pady=10)
        Label(self,text='Колір функції:').grid(column=0,row=2,sticky="ew",padx=10,pady=10)
        drop3.grid(column=1,row=2,sticky="ew",padx=10,pady=10)
        show3.grid(column=2,row=2,sticky="ew",padx=10,pady=10)
        chec1.grid(column=0,row=3)
        chec2.grid(column=1,row=3)
        apply.grid(column=2,row=4)

        updateShow()

class Tutorial(Toplevel):
    def __init__(self,master):
        Toplevel.__init__(self)
        tutorial_text = """
        \tІнкремент Х - дає змогу змінити збільшити якість зображеної функції.\n
        \tФактор Х - дає змогу змінити частоту функції.\n
        \tАмплітуда Y - дає змогу змінити амплітуду функції.\n
        \tЗміщення Х - дає змогу точніше здвинути функцію по ОХ.\n
        \tАнімувати - при зміні анімує функцію.\n
        \tВідображати центральну лінію - при активному стані кожне оновлення
        малюється горизонтальна центральна лінія.\n
        \tВідображати вертикальну лінію - при активному стані кожне оновлення
        малюється вертикальна центральна лінія.\n
        \tФункція: sin(x),cos(x)... - дає змогу вибрати тип зображуваної функції.\n
        \tТочки - список всіх точок на графіку. При виборі точки, вона 
        зображується на графіку.\n
        \tНалаштування - кнопка, яка показує вікно налаштувань.\n
        \tПоказати JSON - кнопка, яка показує координати всіх точок у форматі JSON.\n
        """
        self.geometry('480x400')
        self.resizable(False,False)
        self.attributes('-topmost','true')
        self.title('Як користуватися')
        Label(self,text=tutorial_text).pack(fill=BOTH,expand=0)
        master.eval(f'tk::PlaceWindow {str(self)} center')

class About(Toplevel):
    def __init__(self,master):
        Toplevel.__init__(self)
        about = """
        Графік функції
        Створив Денис Мітленко
        2020 рік
        """
        self.geometry('280x80')
        self.resizable(False,False)
        self.attributes('-topmost','true')
        self.title('Про програму')
        Label(self,text=about).pack(fill=BOTH,expand=0)
        master.eval(f'tk::PlaceWindow {str(self)} center')

class MainWindow(Tk):

    x_inc = 1
    x_fac = 0.04
    x_bias = -18.1
    y_amp = 80
    width = 592
    height = 642
    anim = 0
    my_func = 'x'

    grid_color  = '#dddddd'
    lines_color = '#aaaaff'
    func_color  = '#008000'

    default_grid_color  = '#dddddd'
    default_lines_color = '#aaaaff'
    default_func_color  = '#008000'

    window_width  = 800
    window_height = 592

    def __init__(self,parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.center = self.height//2
        self._do()

    def _do(self):
        def invert_color(color):
            if type(color) == str: rgb = canvas.winfo_rgb(color)
            else: rgb = color
            rgb = (65535-rgb[0], 65535-rgb[1], 65535-rgb[2])
            tk_rgb = "#%04x%04x%04x" % (rgb)
            return tk_rgb

        def invert_canvas():
            if invertCanvas.get():
                items = canvas.find_withtag('all')
                for item in items:
                    fill = canvas.itemcget(item, "fill")
                    if fill != '': fill = invert_color(fill)
                    if canvas.type(item) in ['rectangle','arc']:
                        outline = canvas.itemcget(item, "outline")
                        outline = invert_color(outline)
                        canvas.itemconfig(item, fill=fill, outline=outline)
                    else:
                        canvas.itemconfig(item, fill=fill) 

        def drawGrid():
            canvas.create_rectangle(0, 0, self.width, self.height, fill='#ffffff')
            for x in range(0,self.width,8):
                canvas.create_line(x, 0, x, self.height, fill=self.grid_color)
            for y in range(0,self.height+1,8):
                canvas.create_line(0, y, self.width, y, fill=self.grid_color)
                
        def drawData():
            if enableDataDrawing.get():
                string = 'x_inc=' + str(self.x_inc) + '\nx_fac=' + str(round(self.x_fac,2)) + '\ny_amp=' + str(self.y_amp) + '\nx_bias=' + str(round(self.x_bias,2)) + '\nframe=' + str(int(self.anim*40))
                canvas.create_text(10,20,anchor=NW,text=string,font=("Arail", 8))

        def drawSin():
            xy1 = []
            fun = { 0:lambda x: sin(x), 1:lambda x: cos(x), 2:lambda x: tan(x),3:None }[funcType.get()]
            typ = ['sin(x)','cos(x)','tg(x)',self.my_func][funcType.get()]
            for x in range(self.width):
                xy1.append(x * self.x_inc)
                if funcType.get() == 3:
                    try:
                        xy1.append(int(eval(myFuncVar.get()) + 25))
                    except Exception as e:
                        print('Exception [136]:',e)
                else:
                    xy1.append(int(fun((x * self.x_fac) + self.x_bias + self.anim) * self.y_amp) + self.center)
            canvas.create_line(xy1,fill=self.func_color)
            canvas.create_text(10,self.height-29,anchor=NW,text='y = '+typ,font=("Arail", 14))
            self.dots = xy1
            drawLines()
            invert_canvas()

        def drawLines():
            if cLineEnable.get(): canvas.create_line(0, self.center, self.width, self.center, fill=self.lines_color)
            if cVertEnable.get(): canvas.create_line(self.width//2, 0, self.width//2, self.height, fill=self.lines_color)

        def update(event=None):
            canvas.delete("all")
            drawGrid()
            drawData()
            drawSin()
            lb1.delete(0,END)
            for i in range(0,len(self.dots)-1,2):
                string = str(self.dots[i]) + ' : ' + str(self.dots[i+1])
                lb1.insert(i-1,string)
            b2.config(state=ACTIVE)
            self.ar = []
            for i in range(0,len(self.dots)-1,2):
                self.ar.append( [self.dots[i],self.dots[i+1]] )
        
        def bs1_change(event):
            self.x_inc = event.value
            update()

        def bs2_change(event):
            self.x_fac = event.value
            update()

        def bs3_change(event):
            self.y_amp = event.value
            update()
        
        def bs4_change(event):
            self.x_bias = event.value
            update()

        def point(pointCoord,size):
            x1, y1 = (pointCoord[0] - size), (pointCoord[1] - size)
            x2, y2 = (pointCoord[0] + size), (pointCoord[1] + size)
            canvas.create_oval(x1, y1, x2, y2, fill="#f44336")

        def listSelect(event):
            try:
                pointCoord = [int(i) for i in lb1.get(lb1.curselection()).split(' : ')]
                canvas.delete("all")
                drawGrid()
                drawData()
                drawSin()
                point(pointCoord,3)
                canvas.create_text(pointCoord[0] + 5,pointCoord[1] - 24,anchor=NW,text='(%i,%i)'%(pointCoord[0],pointCoord[1]),font=("Arail", 10))
            except:
                pass
            
        def showJson():
            top = Toplevel(self)
            tx1 = TextScroll(top)
            top.title('Точки у форматі JSON')
            top.geometry('290x220')
            tx1.pack(fill=BOTH,expand=1)
            tx1.txt.delete(0.0,END)
            ar = []
            for i in range(0,len(self.dots)-1,2):
                ar.append( [self.dots[i],self.dots[i+1]] )
            try:
                tx1.txt.insert(0.0,dumps(ar))
            except:
                top.withdraw()

        def animate(*args):
            self.anim = animVar.get()/40
            update()

        def func_write(*args):
            a = ''
            if funcType.get() == 3:
                e1.config(state=ACTIVE)
                a = 'disable'
            else:
                e1.config(state=DISABLED)
                a = 'enable'
            for child in bs1.winfo_children():
                child.configure(state = a)
            for child in bs2.winfo_children():
                child.configure(state = a)
            for child in bs3.winfo_children():
                child.configure(state = a)
            for child in bs4.winfo_children():
                child.configure(state = a)
            s1.configure(state=a)
            l1.configure(state=a)
            update()

        def e1_ret(*args):
            self.my_func = myFuncVar.get()
            update()

        def canvas_motion(event):
            for i in self.ar:
                if sqrt((event.x - i[0]) ** 2 + (event.y - i[1]) ** 2) <= 4:
                    pointCoord = i
                    canvas.delete("all")
                    drawGrid()
                    drawData()
                    drawSin()
                    point(pointCoord,3)
                    canvas.create_text(i[0] + 5,i[1] - 24,anchor=NW,text='(%i;%i)'%(i[0],i[1]),font=("Arail", 10))

        def initMenu():
            menubar = Menu(self)
            self.config(menu=menubar)

            fileMenu = Menu(menubar, tearoff=False)
            fileMenu.add_command(label="Налаштування",command=lambda: Settings(self,update))
            fileMenu.add_command(label="Вийти",command=lambda: self.quit())

            helpMenu = Menu(menubar, tearoff=False)
            helpMenu.add_command(label="Інструкція",command=lambda:Settings(self,update))
            helpMenu.add_command(label="Про програму",command=lambda: About(self))

            menubar.add_cascade(label="Файл", menu=fileMenu)
            menubar.add_cascade(label="Допомога", menu=helpMenu)
        
        def initMenuEvents():
            self.bind('<Control-q>',lambda i: self.quit())
            self.bind('<Control-,>',lambda i: Settings(self,update))
            self.bind('<Control-h>',lambda i: Tutorial(self))

        cLineEnable = IntVar()
        funcType = IntVar()
        cVertEnable = IntVar()
        animVar = DoubleVar()
        enableDataDrawing = IntVar()
        invertCanvas = IntVar()
        myFuncVar = StringVar()

        cLineEnable.set(1)
        funcType.set(0)
        cVertEnable.set(1)
        animVar.set(0)
        enableDataDrawing.set(0)
        invertCanvas.set(0)
        myFuncVar.set(self.my_func)
        animVar.trace_add("write",animate)
        
        canvas = Canvas(self, width = self.width, height = self.height,borderwidth=2, relief="groove")
        self.c = controlFrame = LabelFrame(self,text='Властивості')

        bs1 = ButtonSlider(controlFrame,1,self.x_inc,100,1,'Інкремент Х',bs1_change)
        bs2 = ButtonSlider(controlFrame,0.01,self.x_fac,1,0.00,'Фактор Х',bs2_change)
        bs3 = ButtonSlider(controlFrame,5,self.y_amp,500,5,'Амплітуда Y',bs3_change)
        bs4 = ButtonSlider(controlFrame,0.01,self.x_bias,30,-30,'Зміщення Х',bs4_change)
        s1  = Scale(controlFrame,from_=0,to=249,orient=HORIZONTAL,variable=animVar,length=180)
        b2  = Button(controlFrame,text='Показати JSON',command=showJson,state=DISABLED,width=16)
        c1  = Checkbutton(controlFrame,text='Відображати центральну лінію',onvalue=1,offvalue=0,variable=cLineEnable)
        c2  = Checkbutton(controlFrame,text='Відображати вертикальну лінію',onvalue=1,offvalue=0,variable=cVertEnable)
        r1  = Radiobutton(controlFrame,text='sin(x)',variable=funcType,value=0)
        r2  = Radiobutton(controlFrame,text='cos(x)',variable=funcType,value=1)
        r3  = Radiobutton(controlFrame,text='tg(x)',variable=funcType,value=2)
        r4  = Radiobutton(controlFrame,text='Своя функція:',variable=funcType,value=3)
        e1  = Entry(controlFrame,textvariable=myFuncVar,state=DISABLED)
        l1  = Label(controlFrame,text='Анімувати:')
        lb1 = Listbox(controlFrame,width=31,height=8)
        
        lb1.bind('<<ListboxSelect>>',listSelect)
        e1.bind('<Return>',e1_ret)
        self.bind("<Visibility>", update)
        canvas.bind('<Motion>',canvas_motion)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)
        
        
        funcType.trace_add('write',func_write)
        drawGrid()
        drawLines()

        controlFrame.pack(side=LEFT,fill=Y)
        bs1.grid(column=0,row=0,sticky=NW)
        bs2.grid(column=0,row=1,sticky=NW)
        bs3.grid(column=0,row=2,sticky=NW)
        bs4.grid(column=0,row=3,sticky=NW)
        l1.grid(column=0,row=4,sticky=NW)
        s1.grid(column=0,row=5)
        c1.grid(column=0,row=6,sticky=NW)
        c2.grid(column=0,row=7,sticky=NW)
        Label(controlFrame,text='Функція:').grid(column=0,row=8,sticky=NW)
        r1.grid(column=0,row=9,sticky=NW)
        r2.grid(column=0,row=10,sticky=NW)
        r3.grid(column=0,row=11,sticky=NW)
        r4.grid(column=0,row=12,sticky=NW)
        e1.grid(column=0,row=13,sticky=NW,padx=(20,0))
        Label(controlFrame,text='Точки:').grid(column=0,row=14,sticky=NW)
        lb1.grid(column=0,row=15,sticky=NW)
        b2.grid()

        Tutorial(self)
        initMenu()
        initMenuEvents()
        

if __name__ == '__main__':
    app = MainWindow(None)
    app.resizable(False, False)
    app.title('Графік функцій')
    app.geometry('800x642')
    app.eval('tk::PlaceWindow . center')
    app.mainloop()