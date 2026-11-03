from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
nul=True
z=""
number1=""
number2=""
type_first_number=True
show_znak=True
def click(button):
    user=button["text"]
    global nul,number1,number2
    if nul==True:
        nul=False
        v["text"]=user
    else:
        v["text"]+=user
    if type_first_number==True:
        number1=v['text']
    else:
        number2+=user
    print(number1)
    print(number2)
def znak(button):
    global z, show_znak,type_first_number
    if show_znak==True:
        z=button["text"]
        v["text"]+=z
        show_znak= False
        type_first_number=False

def eguel():
    global show_znak,number1,number2
    if z=="+":
        v["text"]=str(float(number1)+float(number2))

    if z=="-":
        v["text"]=str(float(number1)-float(number2))

    if z=="x":
        v["text"]=str(float(number1)*float(number2))

    if z=="/":
            v["text"]=str(float(number1)/float(number2))
    show_znak=True
    number1=float(v['text'])
    number2=""
def clear():
        global show_znak,type_first_number,number1,number2
        v["text"]=""
        show_znak=True
        type_first_number=True
        number1="" 
        number2=""
        







app=Tk()
app.geometry("500x800")
a=Button(text="1",width=50,bg="#86DAE3",command=lambda: click(a))
a.place(x=30,y=200)

b=Button(text="2",width=50,bg="#86DAE3",command=lambda: click(b))
b.place(x=90,y=200)

c=Button(text="3",width=50,bg="#86DAE3",command=lambda: click(c))
c.place(x=150,y=200)

d=Button(text="4",width=50,bg="#86DAE3",command=lambda: click(d))
d.place(x=30,y=250)

e=Button(text="5",width=50,bg="#86DAE3",command=lambda: click(e))
e.place(x=90,y=250)

f=Button(text="6",width=50,bg="#86DAE3",command=lambda: click(f))
f.place(x=150,y=250)

g=Button(text="7",width=50,bg="#86DAE3",command=lambda: click(g))
g.place(x=30,y=300)

h=Button(text="8",width=50,bg="#86DAE3",command=lambda: click(h))
h.place(x=90,y=300)

i=Button(text="9",width=50,bg="#86DAE3",command=lambda: click(i))
i.place(x=150,y=300)


j=Button(text="+",width=60,bg="#86DAE3",command=lambda: znak(j))
j.place(x=230,y=200)

l=Button(text="-",width=60,bg="#86DAE3",command=lambda: znak(l))
l.place(x=230,y=250)

m=Button(text="x",width=60,bg="#86DAE3",command=lambda: znak(m))
m.place(x=230,y=300)

n=Button(text="/",width=50,bg="#86DAE3",command=lambda: znak(n))
n.place(x=150,y=350)

o=Button(text="=",width=60,bg="#BC86E3",command=lambda: eguel())
o.place(x=230,y=350)

p=Button(text="0",width=50,bg="#86DAE3",command=lambda: click(p))
p.place(x=90,y=350)

w=Button(text="c",width=50,bg="#86DAE3",command=lambda: clear())
w.place(x=30,y=350)

v=Label(text="yeva",width=25,height=5,bg="white",fg="black")
v.place(x=50,y=100)






















app.mainloop()