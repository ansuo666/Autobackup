from tkinter import *
from tkinter import messagebox
import time
import guaqi
import sys
global shi
shi = 86400000
def submit(ev=None): #路径设置
        wj = open('backupconfig.txt','w+')
        wj.write(e1.get())
        wj.write('\n')
        wj.write(e2.get())
        wj.close()
        messagebox.showinfo('信息','路径设置成功！')
def tt(ev=None):  #时钟
   start = time.strftime('%H:%M:%S ',time.localtime(time.time()))
   tishi.config(text = start)
   zhuck.update()
   tishi.after(1000,tt)
def yx(ev=None): #备份脚本启动器的运行
    global shi
    try:
        jg.config(text = '启动成功！')
        result = guaqi.yunxing() #启动器启动
        jg.config(text = result)
        yun.after(shi,yx)
    except:
        result = sys.exc_info()
        jg.config(text = result)
        yun.after(shi,yx)
def tme(ev=None):
    global shi
    val = int(var.get())
    if val == 1:
        shi = 86400000
    elif val == 2:
        shi = 600000
    elif val == 3:
        shi = 1000
zhuck = Tk()
zhuck.resizable(False, False)
var = IntVar()
zhuck.title('自动备份工具') #窗口标题
#zhuck.geometry('800x600') #窗口大小设置
start = time.strftime('%H:%M:%S ',time.localtime(time.time()))
ziti = '楷体 -20'
beilu = Label(zhuck,text = '备份路径',font = ziti) #label
cunlu = Label(zhuck,text = '存档路径',font = ziti)
shiti = Label(zhuck,text = '存档间隔：（若改变时间请再次点击运行）',font = '楷体 -15')
e1 = Entry(zhuck) #输入框
e2 = Entry(zhuck)
butt1 = Button(zhuck,text = '设置',font = ziti,activeforeground = '#000000',activebackground = '#339999',command = submit)
butt2 = Button(zhuck,text = '退出',font = ziti,activeforeground = '#000000',activebackground = '#339999',command = zhuck.quit)
butt3 = Button(zhuck,text = '运行',font = ziti,activeforeground = '#000000',activebackground = '#339999',command = yx)
r1 = Radiobutton(zhuck,text = '一天',variable=var, value=1,command = tme)
r2 = Radiobutton(zhuck,text = '十分钟',variable=var, value=2,command = tme)
r3 = Radiobutton(zhuck,text = '一秒',variable=var, value=3,command = tme)
tishi = Label(zhuck,text = start)
tishi.after(1000,tt)
yun = Label(zhuck,text = '')
jg = Label(zhuck,text = '')
beilu.grid(row = 0)
cunlu.grid(row = 1)
e1.grid(row = 0,column = 1,columnspan = 2)
e2.grid(row = 1,column = 1,columnspan = 2)
butt1.grid(row = 2,column = 0,)
butt3.grid(row = 2,column = 1)
butt2.grid(row = 2,column = 2)
shiti.grid(row = 3,columnspan = 3)
r1.grid(row = 4,column = 0)
r1.select()
r2.grid(row = 4,column = 1)
r3.grid(row = 4,column = 2)
tishi.grid(row = 5,columnspan = 3)
jg.grid(row = 6,columnspan = 3)

zhuck.mainloop()