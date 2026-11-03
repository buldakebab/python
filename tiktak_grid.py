from tkinter import * 
from tkmacosx import Button

app = Tk()
app.geometry('600x600')
a = Button (text="1")
a.grid(row=0,column=0,sticky='nsew')
b= Button (text="2")
b.grid(row=1,column=0,sticky='nsew')
с= Button (text="3")
с.grid(row=1,column=1,sticky='nsew')
for i in range(3):
    app.columnconfigure(i,weight=1)
    app.rowconfigure(i,weight=1)

app. mainloop()
