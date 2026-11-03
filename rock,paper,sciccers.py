from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
import random
def click(button):
    user=button["text"]


    a["bg"]="#B751F0"

    b["bg"]="#B751F0"
    
    c["bg"]="#B751F0"

    button["bg"]="yellow"











    number=random. randint(1,3)


    if number==1:
        e["text"]="computer choice rock"

    elif number==2:
       e["text"]="computer choice paper"

    elif number==3:
        e["text"]="computer choice sciccers"


    if user=="paper" and number==1:
        d["text"]=("user win")
        app ["bg"]="#E68EE3"


    elif user=="paper" and number==2:
        d["text"]=("tie")
        app ["bg"]="#4D62FF"


    elif user=="paper" and number==3:
        d["text"]=("computer win")
        app ["bg"]="#1DE8C6"


    elif user=="rock" and number==1:
        d["text"]="tie"
        app ["bg"]="#4D62FF"
        

    elif user=="rock" and number==2:
        d["text"]="computer wins"
        app ["bg"]="#1DE8C6"


    elif user=="rock" and number==3:
        d["text"]="user win"
        app ["bg"]="#E68EE3"


    elif user=="sciccors" and number==1:
        d["text"]="computer win"
        app ["bg"]="#1DE8C6"


    elif user=="sciccors" and number==2:
        d["text"]="user win"
        app ["bg"]="#E68EE3"


    elif user=="sciccors" and number==3:
        d["text"]="tie"





app=Tk()
app.geometry("800x800")
a=Button(text="rock",width=180,height=150,command=lambda: click(a),bg="#B751F0")
a.place(x=50,y=300)

b=Button(text="paper",width=180,height=150,command=lambda: click(b),bg="#B751F0")
b.place(x=250,y=300)

c=Button(text="sciccors",width=180,height=150,command=lambda: click(c),bg="#B751F0")
c.place(x=450,y=300)

d=Label(text="resolt",bg="white",fg='black')
d.place(x=250,y=200)


e=Label(text="computer choice",bg="white",fg='black')
e.place(x=250,y=100)

















app.mainloop()







