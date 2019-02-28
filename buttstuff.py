import tkinter as tk
import turtle
import math



def clearall():
    global brk
    brk = brk + 1
    t.clear()
    t.pu()
    t.goto(0, 0)
    t.pd()
    t.seth(0)





def goldyboi():
    global size1
    global brk
    t.speed(1000)
    pbrk = brk
    for x in range(size1):
        t.pu()
        t.forward(x)
        t.pd()
        if x > 30:
            t.width(4)
        else:
            t.width(2)
        t.forward(1)
        t.left(222.5)
        if pbrk < brk:
            break
    x = 0
    t.width(2)
    brk = brk + 1
    
    
def wildgoldyboi():
    global size1
    t.speed(1000)
    global brk
    pbrk = brk
    for x in range(size1):
        t.width(1)
        t.forward(x)
        t.pd()
        t.forward(1)
        t.left(222.5)
        if pbrk < brk:
            break
    x = 0
    t.width(2)
    brk = brk + 1




def circleboi():
    global size1
    global brk
    t.pu()
    t.forward(size1)
    t.pd()
    t.left(90)
    t.circle(size1)
    brk = brk + 1





#shape with x sides
def swxs():
    sides = input("How many sides do you want?")
    global size1
    x = 0
    for x in range(size1):
        t.forward(x)
        t.left((360 / int(sides)))

def fbbf():
    colors = ["firebrick", "black", "slate blue", "salmon", "chartreuse"]
    t.pencolor(colors[int(0)])
    
def bbf():
    colors = ["firebrick", "black", "slate blue", "salmon", "chartreuse"]
    t.pencolor(colors[int(1)])
    
def sbbf():
    colors = ["firebrick", "black", "slate blue", "salmon", "chartreuse"]
    t.pencolor(colors[int(2)])

def sbf():
    colors = ["firebrick", "black", "slate blue", "salmon", "chartreuse"]
    t.pencolor(colors[int(3)])

def cbf():
    colors = ["firebrick", "black", "slate blue", "salmon", "chartreuse"]
    t.pencolor(colors[int(4)])


###color buttons
fbb = tk.Button( 
                   text="Firebrick", 
                   fg="Firebrick",
                   command=fbbf)
fbb.grid(row=0, column=0)
bb = tk.Button( 
                   text="Black", 
                   fg="black",
                   command=bbf)
bb.grid(row=0, column=1)
sbb = tk.Button(
                    text="Slate Blue",
                    fg="Slate Blue",
                    command=sbbf)
sbb.grid(row=0, column=2)
sb = tk.Button(
                   text="Salmon",
                   fg="salmon",
                   command=sbf)
sb.grid(row=0, column=3)
cb = tk.Button(
                   text="Chartreuse",
                   fg="Chartreuse",
                   command=cbf)
cb.grid(row=0, column=4)



###shape buttons
sgbb = tk.Button( 
                   text="Golden Spiral", 
                   fg="salmon",
                   command=goldyboi)
sgbb.grid(row=2, column=0)

scb = tk.Button( 
                   text="Circle", 
                   fg="salmon",
                   command=circleboi)
scb.grid(row=2, column=1)

swgbb = tk.Button( 
                   text="Wild Golden Spiral", 
                   fg="salmon",
                   command=wildgoldyboi)
swgbb.grid(row=2, column=2)

gbb = tk.Button( 
                   text="Clear", 
                   fg="salmon",
                   command=clearall)
gbb.grid(row=2, column=3)

quit_button = tk.Button(
                   text="Quit",
                   command=quit)
quit_button.grid(row=3, column=0)


t = turtle.Pen()
t.speed(200)
colors = ["Firebrick", "black", "Slate Blue", "Salmon", "Chartreuse"]
size1 = 100
sides = 0
t.width(2)    
brk = 0
