import turtle
import math
t = turtle.Pen()
t.speed(200)
colors = ["Firebrick", "black", "Slate Blue", "Salmon", "Chartreuse"]
size1 = 500
sides = 0
t.width(2)
#1.shape
#2.color
#3.size
#4.starting

def goldyboi():
    global size1
    t.speed(1000)
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
    x = 0
    t.width(1)

def circleboi():
    global size1
    t.pu()
    t.forward(size1)
    t.pd()
    t.left(90)
    t.circle(size1)




#shape with x sides
def swxs():
    sides = input("How many sides do you want?")
    global size1
    x = 0
    for x in range(size1):
        t.forward(x)
        t.left((360 / int(sides)))

        
def whatsize():
    global size1
    size1 = 100 * int(input("""How large do you want to make your shape
                            1 = Small
                            2 = Medium
                            3 = Large
                            4 = Thicc
                            : """))
#spiral with x sides
def spwxs():
    sides = input("How many sides do you want?")
    t.width(1)
    global size1
    x = 0
    for x in range(size1):
        t.forward(x + 2)
        t.left((360 / int(sides)) + 1)
    t.width(2)


def whatcolor():
    colors = ["firebrick", "black", "slate blue", "salmon", "chartreuse"]
    cs = input("""What color do you want to use?
               0 = Firebrick
               1 = Black
               2 = Slate Blue
               3 = Salmon
               4 = Chartruese
               : """)
    if cs == "1" or "2" or "3" or "4" or "0":
        t.pencolor(colors[int(cs)])
    else:
        whatcolor()
        

def whatshape():
    shape = input("""Select your shape
                  1 = Golden Spiral
                  2 = Shape with x sides
                  3 = Circle
                  4 = Spiral with x sides
                  : """)
    if shape == "1":
        goldyboi()
    elif shape == "2":
        swxs()
    elif shape == "3":
        circleboi()
    elif shape == "4":
        spwxs()
    else:
        whatshape()

def startpos():
    startx = int(input("What x value do you want to start at?: "))
    starty = int(input("What y value do you want to start at?: "))
    t.pu()
    t.goto(startx, starty)
    t.pd()
    t.seth(0)

def redo():
    clear = input("""Do you want to draw a new shape?
                  1 = yes
                  2 = no
                  : """)
    if clear == "2":
        print("Goodbye")
    elif clear == "1":
        clear = input("""Do you want to clear the previous drawings?
                      1 = yes
                      2 = no
                      : """)
        if clear == "1":
            t.clear()
        elif clear == "2":
            print("Cool Cool")
        else:
            redo()
        startxy = input("""Do you want to start where the previous drawing ended?
                        1 = yes
                        2 = no
                        : """)
        if startxy == "1":
            system()
        elif startxy == "2":
            startpos()
            system()
        else:
            redo()
    else:
        redo()



def system():
    whatcolor()
    whatsize()
    whatshape()
    redo()
    
startpos()
system()
