from tkinter import *
import random
root=Tk()
root.title("block")
root.geometry("700x700")
num=0
def action():
    num=random.randint(1,6)
    print(num)
    if num==1:
        buttom_1.config(bg="black")
    else:
        pass
#buttons
buttom_1=Button(root,text="0",padx=50,pady=50)
buttom_2=Button(root,text="1",padx=50,pady=50)
buttom_3=Button(root,text="2",padx=50,pady=50)
buttom_4=Button(root,text="3",padx=50,pady=50)
buttom_5=Button(root,text="4",padx=50,pady=50)
buttom_6=Button(root,text="5",padx=50,pady=50)

dice=Button(root,text="dice",padx=40,pady=30,command=action)
#position
buttom_1.grid(row=0,column=0)
buttom_2.grid(row=0,column=1)
buttom_3.grid(row=0,column=2)
buttom_4.grid(row=0,column=3)
buttom_5.grid(row=0,column=4)
buttom_6.grid(row=0,column=5)
dice.grid(row=1,columnspan=5)

root.mainloop()