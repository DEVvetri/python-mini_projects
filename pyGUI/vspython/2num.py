from tkinter import *
root=Tk()
root.title("vv_call")
root.geometry('1980x1080')
#root.configure(bg="gray")
#==function-----
def but_et1():
    a=e1.get()
    global A
    A=int(a)
    e1.delete(0,END)

def but_et2():
    b=e2.get()
    global B
    B=int(b)
    e2.delete(0,END)

def but_et3():
    op=e3.get()
    e3.delete(0,END)
    global OP
    OP=str(op)
    if OP=="+":
        sum=A+B
        e4.insert(0,sum)
    elif OP=="-":
        sub=A-B
        e4.insert(0,sub)
    elif OP=="x":
        mul=A*B
        e4.insert(0,mul)
    elif OP=="/":
        div=A/B
        e4.insert(0,div)
    elif OP=="%":
        rim=A%B
        e4.insert(0,rim)
    else:
        e4.insert(0,"PLZZ ENTER CORRECT OPERATION")

def cler_but():
    e4.delete(0,END)

def dess():
    root.destroy()

#----label and 
sam=Label(root,text="            ")
l1=Label(root,text="A",font=(20))
l2=Label(root,text="b",font=(20))
l3=Label(root,text="START OPERATION LIKE '+','-','/','x','%'",font=(20))
output=Label(root,text="OUTPUT",font=(20))

# entry--------
e1=Entry(root,border=5)
e2=Entry(root,border=5)
e4=Entry(root,border=5,width=100)
e3=Entry(root,border=5)

#Button----------
b1=Button(root,text="enter",padx=20,pady=5,bg="gold",command=but_et1)
b2=Button(root,text="enter",padx=20,pady=5,bg="gold",command=but_et2)
b3=Button(root,text="LET\'S GO",padx=20,pady=5,bg="gold",command=but_et3)
clear_bt=Button(root,text="CLEAR",bg="blue",command=cler_but)
des_bt=Button(root,text="I WILL DESTROY YOUR WINDOW",padx=60,pady=15,bg="red",command=dess)

#----position
sam.pack(pady=50)
l1.pack()
e1.pack() 
b1.pack()
l2.pack()
e2.pack()
b2.pack(pady=5)
l3.pack()
e3.pack()
b3.pack(pady=5)
output.pack()
e4.pack()
clear_bt.pack()
des_bt.pack(pady=20)
root.mainloop()