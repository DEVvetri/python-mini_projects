from tkinter import *
#-------creation---------
root=Tk()
#-------title and size------
root.title("VV_GUI")
root.geometry('1920x1080')
#--------functions over------------


def sub_but():
    #h="helo"+e1.get()
        name=e1.get()
        passWod=e2.get()
        if name=="vetri"and passWod=="vvgamer":
            r=Tk()
            r.title("vetri")
            l=Label(r,text="successfully submited")
            l.pack()
            r.mainloop()
        if name=="subi"and passWod=="my_best_friend":
            r=Tk()
            r.title("vetri")
            l=Label(r,text="WELCOME BACK SUBI...HAPPY TO SEE YOU",font=('Arial',40))
            l.pack()
            r.mainloop()
        else:
              eror=Label(root,text="INVALID USER")
              eror.pack()
#--------WIDGETS----------------------
l=Label(root,text="            ",font=(24))#.
l1=Label(root,text="username",font=("courier",24))#.grid(row=0,column=0)
e1=Entry(root,border=5,width=25)#.grid(row=0,column=1)
#e1.insert(0,"enter your name")
l2=Label(root,text="password",font=("courier",24))#.grid(row=1,column=0)
e2=Entry(root,border=5,width=25)#.grid(row=1,column=1)
#e2.insert(0,"password")
b1=Button(root,text="submit",border=4,command=sub_but)#.grid(row=2,column=1)
#--------positions & calls---------
l.pack(pady=100)
l1.pack(pady=8)
e1.pack()
l2.pack(pady=8)
e2.pack()
b1.pack(pady=5)
#-------end funtion----------
root.mainloop()