from tkinter import *
from tkmacosx import Button
import random
x=0
a =0 
colors=[
    "#FFE100", "#FF5145","#6868F7","#F054A8","#43004F","#FAF2F8","#8FD8BB","#541545"



]
def yeva ():
    global x,a
    print ("dyne")
    label["text"]=x
    x+=1
    print (x)
    if x%10==0:
        # number=random.randint (0,4)
        # app["bg"] =  colors[number]
        # app["bg"] =  random.choice(colors)
        app["bg"]=colors[a]
        a+=1
        if a==len(colors):
            a=0

        

app = Tk()
app["bg"] = "#1FADA3"
app.geometry("300x300+800+300")
label=Label(text=0)
label.place (x=50,y=100)
btn= Button(text="pillow",bg= "#0F215C", fg= "#ABFFB8", width= 100,command=yeva ) 
btn.place (x=50,y=150)
app.mainloop()
