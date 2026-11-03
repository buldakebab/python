from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
buttons_color=[0,0,0,0,0,0,0,0,0]
# def pillow2 ():
#     b ["bg"]="red"
# def pillow ():
#     a ["bg"]="red"
color="blue"
def show_winner(winner=None):
    if winner:
        messagebox.showinfo("Winner", winner+ " wins!")
    else:
        messagebox.showinfo("tie","tie")
    restart()
def restart():
    global buttons_color
    a ["bg"]="white"
    b ["bg"]="white"
    c ["bg"]="white"
    d ["bg"]="white"
    e ["bg"]="white"
    f ["bg"]="white"
    g ["bg"]="white"
    h ["bg"]="white"
    i ["bg"]="white"

    buttons_color=[0,0,0,0,0,0,0,0,0]





def click(button,number):
   global color 
   if button['bg']!= 'blue' and button['bg']!='red':
    if color=="blue":
        color ="red"
    else:
        color="blue"
    buttons_color[number]=color
    button["bg"]=color
    print(buttons_color)
    if buttons_color[0]==buttons_color[1]==buttons_color[2]!=0:

        show_winner(buttons_color[1])

    elif buttons_color[3]==buttons_color[4]==buttons_color[5]!=0:

        show_winner(buttons_color[5])
        


    elif buttons_color[6]==buttons_color[7]==buttons_color[8]!=0:
        show_winner(buttons_color[6])


    elif buttons_color[0]==buttons_color[3]==buttons_color[6]!=0:
        show_winner(buttons_color[3])


    elif buttons_color[1]==buttons_color[4]==buttons_color[7]!=0:
       show_winner(buttons_color[7])


    elif buttons_color[2]==buttons_color[5]==buttons_color[8]!=0:
        show_winner(buttons_color[8])


    elif buttons_color[0]==buttons_color[4]==buttons_color[8]!=0:
       show_winner(buttons_color[0])

    elif buttons_color[2]==buttons_color[4]==buttons_color[6]!=0:
        show_winner(buttons_color[4])

    elif 0 not in buttons_color:
        show_winner()





def q1():
    click(a,0)
# lambda : click(a,0)
def q2():
    click(b,1)
def q3():
    click (c,2)
def q4():
    click (d,3)
def q5():
    click (e,4)
def q6():
    click (f,5)
def q7():
    click (g,6)
# def q8():
#     click (h,7)
def q9():
    click (i,8)
app=Tk()
app.geometry("600x600")
a=Button(text=1,width=180,height=150,command=1)
a['command']=q1
a.place(x=20,y=20)
b=Button(text=2,width=180,height=150,command=q2)
b.place(x=210,y=20)

c=Button(text=3,width=180,height=150,command=q3)
c.place(x=400,y=20)

d=Button(text=4,width=180,height=150,command=q4)
d.place(x=20,y=210)

e=Button(text=5,width=180,height=150,command=q5)
e.place(x=210,y=210)

f=Button(text=6,width=180,height=150,command=q6)
f.place(x=400,y=210)

g=Button(text=7,width=180,height=150,command=q7)
g.place(x=20,y=400)

h=Button(text=8,width=180,height=150,command=lambda:click(h,7))
h.place(x=210,y=400)

i=Button(text=9,width=180,height=150,command=q9)
i.place(x=400,y=400)



app.bind("1", lambda e:q1())
app.bind("2", lambda e:q2())
app.bind("3", lambda e:q3())
app.bind("4", lambda e:q4())
app.bind("5", lambda e:q5())
app.bind("6", lambda e:q6())
app.bind("7", lambda e:q7())
app.bind("8", lambda e:q8())
app.bind("9", lambda e:q9())























app.mainloop()
