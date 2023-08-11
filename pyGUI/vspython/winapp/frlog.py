from tkinter import *
from tkinter import messagebox
#root-details
r1=Tk()
r1.geometry('1920x1080')
r1.title("login_page")
r1.configure(bg="#00ffff")
#functions
def submit():
    name=e1.get()
    passWod=e2.get()
    #user vetrivel-----------
    if name=="vetri" and passWod=="vvgamer":
        r1.destroy()
        #r2 details
        r2=Tk()
        r2.geometry('1920x1080')
        r2.title("WELCOME back "+"vetri")
        r2.configure(bg="#ffffff")
        #r2--functions

        #r2--widget-frame

        r2f1=LabelFrame(r2,text="LOGIN TO CONTINUE",padx=100,pady=100)
        r2f2=LabelFrame(r2,text="LOGIN TO CONTINUE",padx=100,pady=100)
        r2f3=LabelFrame(r2,text="LOGIN TO CONTINUE",padx=100,pady=100)
        #r2--widget-label
        r2l0=Label(r2f2,text="vanga bro epadi eruka",font=('Arial',15))
        r2l1=Label(r2f1,text="Username",font=('Arial',15),fg="#003311")
        r2l2=Label(r2f2,text="Username",font=('Arial',15),fg="#003311")
        r2l3=Label(r2f3,text="Username",font=('Arial',15),fg="#003311")

        #r2--widget-entry


        #r2--widget-button


        #r2--position
        r2f1.grid(row=0,column=0,padx=25,pady=25)
        r2f2.grid(row=0,column=1,padx=20,pady=20)
        r2f3.grid(row=0,column=2,padx=25,pady=25)
        r2l0.grid(row=0,column=0)
        r2l1.grid(row=1,column=0)
        r2l2.grid(row=1,column=0)
        r2l3.grid(row=0,column=0)
        #end
        r2.mainloop()
    #user subi-----------
    # if name=="subi"and passWod=="bestie":
    #     r1.destroy()
    #     #r2 details
    #     r2=Toplevel()
    #     r2.geometry('1920x1080')
    #     r2.title("WELCOME")
    #     r2.configure(bg="#00ffff")
    #     #r2--functions

    #     #r2--widget-frame
        

        
    #     #r2--widget-label
    
        
    #     #r2--widget-entry


    #     #r2--widget-button


    #     #r2--position
        
    #     r2.mainloop()
    elif name !="vetri" and passWod !="vvgamer":
        messagebox.showerror("invalid","invalid user")

    

#widget-frame
f1=LabelFrame(r1,text="LOGIN TO CONTINUE",padx=90,pady=80)

#widget-label
l1=Label(f1,text="Username",font=('Arial',15),fg="#003311")
l2=Label(f1,text="Password",font=('Arial',15),fg="#003311")

#widget-entry
e1=Entry(f1,font=('Arial',10),border=5)
e2=Entry(f1,font=('Arial',10),show="*",border=5)

#widget-button
b1=Button(f1,text="submit",font=('Arial',10),command=submit)

#position
f1.pack(padx=200,pady=250)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
b1.grid(row=2,column=1)
#END
r1.mainloop()