from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox
#root-details
r1=Tk()
r1.geometry('1920x1080')
r1.title("login_page")
r1.config(bg="#00ffff")
r1.iconbitmap("img\logo.ico")
#functions
def descide():
    palyer_1_num=e1.get()
    palyer_2_num=e2.get()
    count=palyer_1_num+palyer_2_num
    if count%2==0:
        pass
    else:
        pass
#widget-frame
f1=LabelFrame(r1,text="ODD OR EVEN",padx=90,pady=80)

#widget-label
l1=Label(f1,text="PLAYER_1",font=('Arial',15),fg="#003311")
l2=Label(f1,text="PLAYER_2",font=('Arial',15),fg="#003311")

#widget-entry
e1=Entry(f1,font=('Arial',10),show="*",border=5)
e2=Entry(f1,font=('Arial',10),show="*",border=5)

#widget-button
b1=Button(f1,text="submit",font=('Arial',10),command=descide)

#position
f1.pack(padx=200,pady=250)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
b1.grid(row=2,column=1)
#END
r1.mainloop()