from tkinter import *
global shi
shi = 86400000
def resize(ev=None):
    hello.config(font='楷体 -%d' % sc.get())
def changelabel(ev=None):
    hello.config(text = '很棒')
def seeet(ev=None):
    global shi
    if int(var.get()) == 1:
        shi = 123456
        st = 'you selected' + str(shi)
        ceshi.config(text = st)
ziti = '楷体'
top = Tk()
var = IntVar()
top.title('Main')
top.geometry('800x420')
hello = Label(top,text = '你好 世界',font = '楷体 -40',activebackground = 'red')
hello.grid(row = 0,columnspan = 2)
oneday = Radiobutton(top,text = 'oneday',variable=var, value=1,command = seeet)
butt = Button(top,text = '退出',command = top.quit,font = '楷体 -20',activeforeground = 'white',activebackground = 'grey')
butt1 = Button(top,text = '提交',command = changelabel,font = '楷体 -20',activeforeground = '#000000',activebackground = '#339999')
butt1.grid(row = 1,column = 0)
butt.grid(row = 1,column = 1)
sc = Scale(top,from_ = 20 , to = 100,orient =HORIZONTAL,command =resize)
sc.grid(row = 3,columnspan = 2)
sc.set(40)
ceshi = Label(top,text = str(shi))
oneday.select()
oneday.grid(row = 4,column = 0)
ceshi.grid(row = 4,column = 1)

top.mainloop()