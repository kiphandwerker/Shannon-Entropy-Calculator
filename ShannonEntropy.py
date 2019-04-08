import math
import numpy as np
import pyautogui
from tkinter import *

def show_answer():
    Genesum = int(Aentry.get()) + int(Centry.get()) + int(Gentry.get()) + int(Tentry.get())

    APa = int(Aentry.get())/Genesum
    AP.insert(0, APa)
    CPa = int(Centry.get())/Genesum
    CP.insert(0, CPa)
    GPa = int(Gentry.get())/Genesum
    GP.insert(0, GPa)
    TPa = int(Tentry.get())/Genesum
    TP.insert(0, TPa)

    Alog2a = math.log(APa + 0.01, 2)
    Alog2.insert(0, Alog2a)
    Clog2a = math.log(CPa + 0.01, 2)
    Clog2.insert(0, Clog2a)
    Glog2a = math.log(GPa + 0.01, 2)
    Glog2.insert(0, Glog2a)
    Tlog2a = math.log(TPa + 0.01, 2)
    Tlog2.insert(0, Tlog2a)

    APloga = Alog2a * APa
    APlog.insert(0, APloga)
    CPloga = Clog2a * CPa
    CPlog.insert(0, CPloga)
    GPloga = Glog2a * GPa
    GPlog.insert(0, GPloga)
    TPloga = Tlog2a * TPa
    TPlog.insert(0, TPloga)

    Asuma = APloga + CPloga + GPloga + TPloga
    Asum.insert(0, Asuma)

    Abitsa = 2 + Asuma
    Abits.insert(0, Abitsa)

    Aheighta = Abitsa * APa
    Aheight.insert(0, Aheighta)
    Cheighta = Abitsa * CPa
    Cheight.insert(0, Cheighta)
    Gheighta = Abitsa * GPa
    Gheight.insert(0, Gheighta)
    Theighta = Abitsa * TPa
    Theight.insert(0, Theighta)



def reset():
    pyautogui.alert(text='Resetting Values', title='Reset', button='OK')
    Aentry.delete(0, 'end'); Centry.delete(0, 'end'); Gentry.delete(0, 'end'); Tentry.delete(0, 'end')
    AP.delete(0, 'end'); CP.delete(0, 'end'); GP.delete(0, 'end'); TP.delete(0, 'end')
    Alog2.delete(0, 'end'); Clog2.delete(0, 'end'); Glog2.delete(0, 'end'); Tlog2.delete(0, 'end')
    APlog.delete(0, 'end'); CPlog.delete(0, 'end'); GPlog.delete(0, 'end'); TPlog.delete(0, 'end')
    Asum.delete(0, 'end'); Abits.delete(0, 'end')
    Aheight.delete(0, 'end'); Cheight.delete(0, 'end'); Gheight.delete(0, 'end'); Theight.delete(0, 'end')


root = Tk()
root.geometry('1200x250')
root.title('Shannon Entropy Calculator')
space = Label(root, text='')
space.grid(row=0, column=2)

A = Label(root, text='A', font='bold')
A.grid(row=1, column=0)
C = Label(root, text='C', font='bold')
C.grid(row=2, column=0)
G = Label(root, text='G', font='bold')
G.grid(row=3, column=0)
T = Label(root, text='T', font='bold')
T.grid(row=4, column=0)


counts = Label(root, text='Counts', font='bold')
counts.grid(row=0, column=1)
Aentry = Entry(root, bg='lightgreen')
Aentry.grid(row=1, column=1)
Centry = Entry(root, bg='lightgreen')
Centry.grid(row=2, column=1)
Gentry = Entry(root, bg='lightgreen')
Gentry.grid(row=3, column=1)
Tentry = Entry(root, bg='lightgreen')
Tentry.grid(row=4, column=1)


Pbase = Label(root, text='P(base)', font='bold')
Pbase.grid(row=0, column=2)
AP = Entry(root, text=Aentry.get())
AP.grid(row=1, column=2)
CP = Entry(root, text=Aentry.get())
CP.grid(row=2, column=2)
GP = Entry(root, text=Aentry.get())
GP.grid(row=3, column=2)
TP = Entry(root, text=Aentry.get())
TP.grid(row=4, column=2)

log2 = Label(root, text='log2(Pbase)', font='bold')
log2.grid(row=0, column=3)
Alog2 = Entry(root, text=Aentry.get())
Alog2.grid(row=1, column=3)
Clog2 = Entry(root, text=Aentry.get())
Clog2.grid(row=2, column=3)
Glog2 = Entry(root, text=Aentry.get())
Glog2.grid(row=3, column=3)
Tlog2 = Entry(root, text=Aentry.get())
Tlog2.grid(row=4, column=3)

Plog = Label(root, text='P*log2P', font='bold')
Plog.grid(row=0, column=4)
APlog = Entry(root, text=Aentry.get())
APlog.grid(row=1, column=4)
CPlog = Entry(root, text=Aentry.get())
CPlog.grid(row=2, column=4)
GPlog = Entry(root, text=Aentry.get())
GPlog.grid(row=3, column=4)
TPlog = Entry(root, text=Aentry.get())
TPlog.grid(row=4, column=4)

Psum = Label(root, text='Sum', font='bold')
Psum.grid(row=0, column=5)
Asum = Entry(root, text=Aentry.get())
Asum.grid(row=1, column=5)

bits = Label(root, text='2+Sum = bits', font='bold')
bits.grid(row=0, column=6)
Abits = Entry(root, text=Aentry.get())
Abits.grid(row=1, column=6)

Height = Label(root, text='Letter Height', font='bold')
Height.grid(row=0, column=7)
Aheight = Entry(root, text=Aentry.get())
Aheight.grid(row=1, column=7)
Cheight = Entry(root, text=Aentry.get())
Cheight.grid(row=2, column=7)
Gheight = Entry(root, text=Aentry.get())
Gheight.grid(row=3, column=7)
Theight = Entry(root, text=Aentry.get())
Theight.grid(row=4, column=7)

Submit = Button(root, text='SUBMIT', command=show_answer)
Submit.grid(row=6, column=1)

Reset = Button(root, text='RESET', command=reset)
Reset.grid(row=7, column=1)

root.mainloop()

