from tkinter import*
#-----root------------
root=Tk()
root.configure(bg="blue")
#-------functions---------
def fn_num1(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def fn_add():
    num1=e.get()
    global A
    global math
    math="addition"
    A=int(num1)
    e.delete(0,END)
    

def fn_sub():
    num1=e.get()
    global A
    global math
    math="subraction"
    A=int(num1)
    e.delete(0,END)

def fn_div():
    num1=e.get()
    global A
    global math
    math="division"
    A=int(num1)
    e.delete(0,END)

def fn_mul():
    num1=e.get()
    global A
    global math
    math="multiplication"
    A=int(num1)
    e.delete(0,END)

def fn_equal():
    num2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,A+int(num2))
    elif math=="subraction":
        e.insert(0,A-int(num2))
    elif math=="multiplication":
        e.insert(0,A*int(num2))
    elif math=="division":
        e.insert(0,A/int(num2))

def fn_clear():
    e.delete(0,END)

def fn_des():
    root.destroy()
#-----labels------------
l1=Label(root,text="-Calculator",bg="blue")
l2=Label(root,text="  ")
e=Entry(root,width=20,font=('Arial',40),borderwidth=15,state="normal")
#-------button---------
but_clr=Button(root,text="clear",font=("Arial",25),border=4,padx=90,pady=20,activebackground="yellow",command=fn_clear)
but_dest=Button(root,text="destroy",font=("Arial",25),border=4,padx=75,pady=20,bg="red",activebackground="orange",command=fn_des)

but_1=Button(root,text="1",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(1))
but_2=Button(root,text="2",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(2))
but_3=Button(root,text="3",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(3))

but_4=Button(root,text="4",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(4))
but_5=Button(root,text="5",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(5))
but_6=Button(root,text="6",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(6))


but_7=Button(root,text="7",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(7))
but_8=Button(root,text="8",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(8))
but_9=Button(root,text="9",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(9))

but_div=Button(root,text="/",font=("Arial",25),border=4,padx=45,pady=20,activebackground="yellow",command=fn_div)
but_zero=Button(root,text="0",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command= lambda: fn_num1(0))
but_dot=Button(root,text=".",font=("Arial",25),border=4,padx=45,pady=20,activebackground="yellow",command= lambda: fn_num1("."))

but_x=Button(root,text="*",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command=fn_mul)
but_sub=Button(root,text="-",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command=fn_sub)
but_add=Button(root,text="+",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command=fn_add)
but_equal=Button(root,text="=",font=("Arial",25),border=4,padx=40,pady=20,activebackground="yellow",command=fn_equal)
#-------position--------------
l1.grid()
e.grid(row=1,column=0,columnspan=4,padx=5)

but_1.grid(row=5,column=0,pady=15)
but_2.grid(row=5,column=1)
but_3.grid(row=5,column=2)
but_add.grid(row=5,column=3)

but_4.grid(row=4,column=0,pady=10)
but_5.grid(row=4,column=1)
but_6.grid(row=4,column=2)
but_sub.grid(row=4,column=3)

but_7.grid(row=3,column=0,pady=10)
but_8.grid(row=3,column=1)
but_9.grid(row=3,column=2)
but_x.grid(row=3,column=3)

but_div.grid(row=6,column=0,pady=10)
but_zero.grid(row=6,column=1)
but_dot.grid(row=6,column=2)
but_equal.grid(row=6,column=3)

but_clr.grid(row=7,column=0,columnspan=2)
but_dest.grid(row=7,column=2,columnspan=2)
#-----END------
root.mainloop()
