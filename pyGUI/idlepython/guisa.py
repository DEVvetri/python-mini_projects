from tkinter import *
#-------creation---------
root=Tk()
#-------title and size------
root.title("VV_GUI")
root.geometry('600x500')
#--------functions over------------
e1=Entry(root,border=5).grid(row=0,column=1)
def sub_but():
    l=Label(root,text="successfully submited").grid()
    
#--------WIDGETS----------------------
l1=Label(root,text="username",font=(24)).grid(row=0,column=0)

l2=Label(root,text="password",font=(24)).grid(row=1,column=0)
e2=Entry(root,border=5).grid(row=1,column=1)
b1=Button(root,text="submit",border=4,command=sub_but).grid(row=2,column=1)
#--------positions & calls---------

#-------end funtion----------
root.mainloop()
