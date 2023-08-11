from tkinter import *
#-------creation---------
root=Tk()
#-------title and size------
root.title("VV_GUI")
root.geometry('600x500')
#--------functions over------------

def sub_but():
    #h="helo"+e1.get()
    l=Label(root,text="successfully submited").grid()
    
#--------WIDGETS----------------------
l=Label(root,text="            ",font=(20))#.
l1=Label(root,text="username",font=("courier",20)).grid(row=0,column=0)
e1=Entry(root,border=5).grid(row=0,column=1)
l2=Label(root,text="password",font=("courier",20)).grid(row=1,column=0)
e2=Entry(root,border=5,fg="blue").grid(row=1,column=1)
b1=Button(root,text="submit",border=4,command=sub_but).grid(row=2,column=1)
#--------positions & calls---------
# l.pack(pady=100)
# l1.pack(pady=8)
# e1.pack()
# l2.pack(pady=8)
# e2.pack()
# b1.pack(pady=5)
#-------end funtion----------
root.mainloop()