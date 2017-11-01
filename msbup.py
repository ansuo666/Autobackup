from tkinter import *
from tkinter import messagebox,ttk
import time
import guaqi
import sys
import threading
import os
global shi
global res

res = 0
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
def yx(): #备份脚本启动器的运行
    global shi
    global res
    try:
        jg.config(text = '备份中！如有卡顿请勿关闭！')
        result = guaqi.yunxing() #启动器启动
        res = 1
        jg.config(text = result)
        p1.config(value = 100)
        yun.after(shi,play)
    except:
        result = sys.exc_info()
        jg.config(text = result)
        yun.after(shi,play)
        p1.config(value = 0)
def tme(ev=None):#备份时间间隔设置
    global shi
    val = int(var.get())
    if val == 1:
        shi = 86400000
    elif val == 2:
        shi = 600000
    elif val == 3:
        shi = 1000

def play(ev=None):
    try:
        threads = []
        t1 = threading.Thread(target=yx)
        threads.append(t1)
        t2 = threading.Thread(target=pro)
        threads.append(t2)
        t3 = threading.Thread(target=tt)
        threads.append(t3)
        if __name__ == '__main__':
            for i in threads:
                i.setDaemon(True)
                i.start()
                zhuck.update()
            p1.config(value = 100)
            jd.config(text = '100')
            p1.stop()
    except:
        messagebox.showinfo('info',sys.exc_info())




def pro(ev=None):
    global res
    try:
        p1.start()
        ppp = [r'',r'']
        i = 0
        for re in open('backupconfig.txt','r+'):
            ppp[i] = re
            i += 1
        pp1 = ppp[0]
        pp2 = ppp[1]
        pp1 = pp1.strip()
        pp2 = pp2.strip() + time.strftime('%Y%m%d',time.localtime(time.time())) +"\\" + time.strftime('%H%M%S',time.localtime(time.time())) + '.tar.gz'
        s1 = getFileSize(pp1)
        #print(pp2)
        for i in range(s1):
            if res != 1:
                s2 = os.path.getsize(pp2)
                jdvalue = (s2/s1)*100
                p1.config(value = jdvalue)
                jd.config(text = '%.3d' % jdvalue)
                zhuck.update()
            else:
                p1.config(value = 100)
                jd.config(text = '100')
                res = 0
                zhuck.update()
    except:
        messagebox.showinfo('info',sys.exc_info())

def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size

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
butt3 = Button(zhuck,text = '运行',font = ziti,activeforeground = '#000000',activebackground = '#339999',command = play)
r1 = Radiobutton(zhuck,text = '一天',variable=var, value=1,command = tme)
r2 = Radiobutton(zhuck,text = '十分钟',variable=var, value=2,command = tme)
r3 = Radiobutton(zhuck,text = '一秒',variable=var, value=3,command = tme)
p1 = ttk.Progressbar(zhuck,orient = "horizontal",mode = 'determinate',length=200,maximum = 100)#进度条
tishi = Label(zhuck,text = start)
tishi.after(1000,tt)
yun = Label(zhuck,text = '')
jg = Label(zhuck,text = '')
jd = Label(zhuck,text = r'000',compound = 'left')
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
p1.grid(row = 6,columnspan = 4)
jd.grid(row = 6,column = 4)
jg.grid(row = 7,columnspan = 3)

zhuck.mainloop()