from tkinter import *
root=Tk()
root.configure(bg="gray")
#root.geometry('1920x1080')
#-----box-------------
e=Entry(root,width=80,borderwidth=6)
#e.insert(0,"0")
e.grid(row=0,column=0,columnspan=4)

#----funtion--------------
def fn_click(number):
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

#--------------labels-------------
#-----button-----------
#---but 1 to 3----------
but_1=Button(root,text="1",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(1))
but_2=Button(root,text="2",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(2))
but_3=Button(root,text="3",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(3))

#---but 4 to 6----------
but_4=Button(root,text="4",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(4))
but_5=Button(root,text="5",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(5))
but_6=Button(root,text="6",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(6))

#---but 7 to 9----------
but_7=Button(root,text="7",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(7))
but_8=Button(root,text="8",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(8))
but_9=Button(root,text="9",border=4,padx=40,pady=20,bg="orange",activebackground="yellow",command=lambda : fn_click(9))

#---but 0,add,mul,equaland destroy----------
but_0=Button(root,text="0",border=4,padx=40,pady=20,bg="pink",activebackground="green",command=lambda : fn_click(0))

but_add=Button(root,text="+",border=4,padx=40,pady=20,bg="pink",activebackground="green",command=fn_add)
but_mul=Button(root,text="x",border=4,padx=40,pady=20,bg="pink",activebackground="green",command=fn_mul)
but_equal=Button(root,text="=",border=4,padx=40,pady=20,bg="pink",activebackground="green",command=fn_equal)

but_clear=Button(root,text="clear",border=3,padx=31,pady=20,bg="pink",activebackground="green",command=fn_clear)
but_stop=Button(root,text="destroy",border=3,padx=87,pady=20,bg="pink",activebackground="red",command=fn_des)


#---------position----------

but_1.grid(row=3,column=0)
but_2.grid(row=3,column=1)
but_3.grid(row=3,column=2)

but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)

but_7.grid(row=1,column=0)
but_8.grid(row=1,column=1)
but_9.grid(row=1,column=2)

but_0.grid(row=5,column=0)
but_add.grid(row=1,column=3)
but_mul.grid(row=2,column=3)
but_clear.grid(row=5,column=1)
but_equal.grid(row=3,column=3)
but_stop.grid(row=5,column=2,columnspan=2)

root.mainloop()