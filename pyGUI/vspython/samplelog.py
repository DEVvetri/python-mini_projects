from tkinter import *
from PIL import *
#----root spec
r=Tk()
r.geometry('1920x1080')
r.iconbitmap('D:/coding learn/pyGUI/vspython/winapp/Fb.ico')
#----functions------
def sub():
    pass
#----labels--------
sam=Label(r,text="                         ",font=('Arial',20),bg="blue")

l1=Label(r,text="username",font=('Arial',20),padx=10)
l2=Label(r,text="password",font=('Arial',20))
#----entry----------
e1=Entry(r,width=25,borderwidth=5)
e2=Entry(r,width=25,borderwidth=5)
#----buttons--------
b1=Button(r,text="submit",font=('Arial',10),padx=5,command=sub)
c1=Checkbutton(r,text="I am not robot",font=('Arial',10),padx=5,pady=5)
#---position---------
#sam.grid(row=0,column=0,columnspan=4)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1,padx=30,pady=15)
e2.grid(row=1,column=1,padx=30,pady=15)
c1.grid(row=2,column=1)
b1.grid(row=3,column=1)
r.mainloop()
#-----END---------
