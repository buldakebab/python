import time
import turtle as t 

def fill(color):
    t.begin_fill ()
    t.color (color)
    t.forward (700)
    t.left (90)
    t.forward (450)
    t.left (90)
    t.forward (1400)
    t.left (90)
    t.forward (450)
    t.left (90)
    t.forward (700)
    t.end_fill ()
fill('aliceblue')
t.left(180)
fill("darksalmon")
t.right(180)

def pyramid(color, size):
    t.begin_fill ()
    t.color (color)
    t.forward (size)
    t.left (120)
    t.forward (size)
    t.left (120)
    t.forward (size)
    t.left (120)
    t.end_fill ()
def change_position(x,y):
    t.penup ()
    t.goto (x, y)
    t.pendown ()

def tree():
    t.begin_fill ()
    t.color ("green")
    t.circle (50)
    t.end_fill ()


    t.color ("brown")
    t.right (90)
    t.forward (100)
    t.left (90)


pyramid(color = "pink", size = 200)
change_position(100,0)
pyramid (color = "red", size = 400)
change_position(350,0)
pyramid (color = "blue", size = 200)
change_position (x= -200, y= - 100)
tree()
change_position (x= -400, y= - 200)
tree()
change_position (x= +27, y= -100)
tree ()
change_position (x= +327, y= -200)
tree()
change_position (x= +12, y= -300)
tree()






t.penup ()
t.goto (-600, 300)
t.pendown ()


t.begin_fill ()
t.color ("yellow")
t.circle (50)
t.end_fill ()

t.penup ()
t.goto (-350, 300)
t.pendown ()




t.begin_fill ()
t.color ("grey")
t.circle (50)
t.end_fill ()

t.penup ()
t.goto (-325, 300)
t.pendown ()





t.begin_fill ()
t.color ("grey")
t.circle (50)
t.end_fill ()


t.penup ()
t.goto (-300, 300)
t.pendown ()



t.begin_fill ()
t.color ("grey")
t.circle (50)
t.end_fill ()


def  bird():

    t.right (45)
    t.forward (50)
    t.left (90)
    t.forward (50)

    t.right (45)



change_position(x=-300,y=250)
bird()

change_position (x=-200,y=250)
bird()

change_position(x=-200,y=150)
bird()






























t.done()