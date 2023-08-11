from tkinter import *
from tkinter import messagebox
root=Tk()

def winTWO():
    name=ent_user.get()
    password=ent_pass.get()
    if name=="vetri"and password=="vv":
        win2=Toplevel()
        win2.geometry('600x500')
        my_lab=Label(win2,text="SUCCESSFULLY login")
        my_lab.pack()
    else:
         messagebox.INFO("error","invalid use")
        
lab_user=Label(root,text="username").pack()
ent_user=Entry(root,width=20).pack()
lab_pass=Label(root,text="password").pack()
ent_pass=Entry(root,width=20).pack()

my_bt=Button(root,text="submit",command=winTWO).pack()
root.mainloop()