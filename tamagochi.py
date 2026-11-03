from tkinter import *
from tkmacosx import Button
from tkinter import messagebox

happy=83
energy=98
satiety=60


app=Tk()
app.geometry ("500x800")
app['bg']='white'
a=Label(text="stjerne")
a.place (x=50,y=50,width=100,height=100)


b=Label(text="happy-83%")
b.place (x=50,y=200,width=100,height=100)


c=Label(text="energy-98%")
c.place (x=50,y=330,width=100,height=100)


d=Label(text="satiety-60%")
d.place (x=50,y=470,width=100,height=100)

def action_eat():
    global happy,energy,satiety
    happy+=5
    print (happy)

    energy-=10
    print (energy)

    satiety+=20
    print (satiety)

    
    b  ["text"] = happy
    c  ["text"] = energy
    d  ["text"] = satiety





def action_play():
    global happy,energy,satiety
    happy+=20
    print (happy)
    energy-=20
    print (energy)
    satiety-=15
    print (satiety)


    b  ["text"] = happy
    c  ["text"] = energy
    d  ["text"] = satiety
    
    



def action_sleep():
    global happy,energy,satiety
    happy-=10
    print (happy)
    energy+=40
    print (energy)
    satiety-=20
    print (satiety)

    b  ["text"] = happy
    c  ["text"] = energy
    d  ["text"] = satiety
    
    



e=Button(text="eat",command=action_eat)
e.place (x=50,y=590,width=100,height=100)


f=Button(text="play",command=action_play)
f.place (x=170,y=590,width=100,height=100)

g=Button(text="sleep",command=action_sleep)
g.place (x=290,y=590,width=100,height=100)



















app.mainloop()