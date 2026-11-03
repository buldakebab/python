from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
import random
game_list= []
user_list = []
step=0
colors={"green":{"normal":"#7EE0B0","active":"#6FC26B"},
        "pink":{"normal":"#E07E9B","active":"#AC467D"},
        "purple":{"normal":"#937EE0","active":"#8C46AC"},
        "yellow":{"normal":"#E0D07E","active":"#EAD72C"},}

def start_game():
    b["state"]="normal"
    c["state"]="normal"
    d["state"]="normal"
    e["state"]="normal"
    global user_list
    user_list =[]
    random_color=random.choice(list(colors.keys()))
    game_list.append(random_color)
    show_buttons_row(0)

    #   btn['bg']=
    f["text"]="choose your buttons"



def show_buttons_row(index=0):
    if index<len(game_list):
        color=game_list[index]
        btn=buttons_color[color]
        btn['bg']='aqua'
        app.after(500,lambda:normal_color(btn,color))
        app.after(1000,lambda:show_buttons_row(index+1))
    else:
        print("user play now")


def normal_color(button,color):
    button['bg']=colors[color]['normal']
def click(button,color):
    global step
    button['bg']=colors [color]["active"]
    user_list.append(color)
    app.after(500,lambda:normal_color(button,color))


    if game_list[step]!=user_list[step]:
        messagebox.showerror("you lose","you lose")
        b["state"]="disabled"
        c["state"]="disabled"
        d["state"]="disabled"
        e["state"]="disabled"
        return
    else:
        step+=1
    if len(user_list)== len(game_list):
        print ("you win")
        step=0
        app. after (1500,lambda:start_game())
    


app=Tk()
app.geometry ("500x800")
a=Button(text="start game",width=400,height=150,bg="blue",command=lambda:start_game())
a. place(x=50,y=50)

b=Button(width=180,height=150,bg=colors["green"]['normal'],command=lambda: click(button=b,color="green"))
b. place(x=50,y=300)


c=Button(width=180,height=150,bg=colors["pink"]['normal'],command=lambda: click(c,"pink"))
c. place(x=250,y=300)

d=Button(width=180,height=150,bg=colors["purple"]['normal'],command=lambda: click(d,"purple"))
d. place(x=50,y=470)

e=Button(width=180,height=150,bg=colors["yellow"]['normal'],command=lambda: click(e,"yellow"))
e. place(x=250,y=470)

f=Label(width=18,height=5,text="yeva",fg="white")
f. place(x=150,y=205)






buttons_color= {"yellow":e,
                "green":b,
                "pink":c,
                "purple":d
                }



























app.mainloop()