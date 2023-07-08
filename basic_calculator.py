from tkinter import *
root=Tk()
root.configure(background="grey")
######
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():#che3cks if it integer
            value=int(scvalue.get())
        else:
            value=eval(screen.get())#evaluates the operation given on screen

        scvalue.set(value)
        screen.update()
    elif text=="C" or text=="CE":
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get()+text)
        screen.update()
root.geometry("400x570")
# root.minsize(400,400)
# root.maxsize(600,600)
root.title("Calculator")
############
# root.wm_iconbitmap("1.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,text=scvalue,font="lucida 40 bold",width=3,bg="black",fg="wheat")
screen.pack(ipadx=150,pady=10,padx=10)#ipadx means screen width from both sides 

f=Frame(root)
b=Button(f,text="%",font="lucida 35 bold",bg="black",fg="wheat",width=3)
# b.grid(row=0,column=0,sticky="NSEW")
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="CE",font="lucida 35 bold",bg="black",fg="wheat",width=3)
# b.grid(row=0,column=1,sticky="NSEW")
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="C",font="lucida 35 bold",bg="black",fg="wheat",width=3)
# b.grid(row=0,column=2,sticky="NSEW")
b.pack(side=LEFT)
b.bind('<Button>',click)

b=Button(f,text="/",font="lucida 35 bold",bg="black",fg="wheat",width=3)
# b.grid(row=0,column=3,sticky="NSEW")
b.pack(side=LEFT)
b.bind('<Button>',click)

f.pack()
######
f=Frame(root)
b=Button(f,text="7",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="8",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="9",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

b=Button(f,text="*",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

f.pack()
########
f=Frame(root)
b=Button(f,text="4",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

b=Button(f,text="5",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="6",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)
 
b=Button(f,text="-",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

f.pack()
########
f=Frame(root)
b=Button(f,text="1",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="2",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="3",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

b=Button(f,text="+",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

f.pack()
#####
f=Frame(root)
b=Button(f,text="+/_",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text="0",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)


b=Button(f,text=".",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

b=Button(f,text="=",font="lucida 35 bold",bg="black",fg="wheat",width=3)
b.pack(side=LEFT)
b.bind('<Button>',click)

f.pack()
######



f.pack()
root.mainloop()