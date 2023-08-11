from tkinter import *
from tkinter import messagebox
import random as rm
#root-details
r2=Tk()
r2.title("bulb game")

vr=0
#functions
def who_is_win():
    pass


#action for blue------------
def active1():
    global vr
    r=rm.randint(0,11)
    for i in range(0,r,1):
        ran_num=rm.randint(0,11)
        if ran_num==1:
            b1=Button(r2,text="1",padx=25,pady=15,border=1,background="blue")
            b1.grid(row=0,column=0,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==2:
            b2=Button(r2,text="2",padx=25,pady=15,border=1,background="blue")
            b2.grid(row=0,column=1,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==3:
            b3=Button(r2,text="3",padx=25,pady=15,border=1,background="blue")
            b3.grid(row=0,column=2,padx=3)
            vr+=1
            who_is_win()

        elif ran_num==4:
            b4=Button(r2,text="4",padx=25,pady=15,border=1,background="blue")
            b4.grid(row=0,column=3,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==5:
            b5=Button(r2,text="5",padx=25,pady=15,border=1,background="blue")
            b5.grid(row=0,column=4,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==6:
            b6=Button(r2,text="6",padx=25,pady=15,border=1,background="blue")
            b6.grid(row=0,column=5,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==7:
            b7=Button(r2,text="7",padx=25,pady=15,border=1,background="blue")
            b7.grid(row=0,column=6,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==8:
            b8=Button(r2,text="8",padx=25,pady=15,border=1,background="blue")
            b8.grid(row=0,column=7,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==9:
            b9=Button(r2,text="9",padx=25,pady=15,border=1,background="blue")
            b9.grid(row=0,column=8,padx=3)
            vr+=1
            who_is_win()
        elif ran_num==10:
            b10=Button(r2,text="10",padx=25,pady=15,border=1,background="blue")
            b10.grid(row=0,column=9,padx=3)
            vr+=1
            who_is_win()
        else:
            l2=Label(r2,text="retry")
            l2.grid(row=2,column=0,columnspan=9)
        
#END action 1-----------
#action2 for green------------
def active2():
    r=rm.randint(1,11)
    for i in range(1,r,1):
        ran_num=rm.randint(0,11)
        if ran_num==1:
            b1=Button(r2,text="1",padx=25,pady=15,border=1,background="green")
            b1.grid(row=0,column=0,padx=3)
        elif ran_num==2:
            b2=Button(r2,text="2",padx=25,pady=15,border=1,background="green")
            b2.grid(row=0,column=1,padx=3)
        elif ran_num==3:
            b3=Button(r2,text="3",padx=25,pady=15,border=1,background="green")
            b3.grid(row=0,column=2,padx=3)

        elif ran_num==4:
            b4=Button(r2,text="4",padx=25,pady=15,border=1,background="green")
            b4.grid(row=0,column=3,padx=3)

        elif ran_num==5:
            b5=Button(r2,text="5",padx=25,pady=15,border=1,background="green")
            b5.grid(row=0,column=4,padx=3)
        elif ran_num==6:
            b6=Button(r2,text="6",padx=25,pady=15,border=1,background="green")
            b6.grid(row=0,column=5,padx=3)

        elif ran_num==7:
            b7=Button(r2,text="7",padx=25,pady=15,border=1,background="green")
            b7.grid(row=0,column=6,padx=3)
        elif ran_num==8:
            b8=Button(r2,text="8",padx=25,pady=15,border=1,background="green")
            b8.grid(row=0,column=7,padx=3)

        elif ran_num==9:
            b9=Button(r2,text="9",padx=25,pady=15,border=1,background="green")
            b9.grid(row=0,column=8,padx=3)

        elif ran_num==10:
            b10=Button(r2,text="10",padx=25,pady=15,border=1,background="green")
            b10.grid(row=0,column=9,padx=3)
        else:
            l2=Label(r2,text="retry")
            l2.grid(row=2,column=0,columnspan=9)
#action2 green END-----------
#action3 for yellow------------
def active3():
    r=rm.randint(0,11)
    for i in range(1,r,1):
        ran_num=rm.randint(1,11)
        if ran_num==1:
            b1=Button(r2,text="1",padx=25,pady=15,border=1,background="yellow")
            b1.grid(row=0,column=0,padx=3)
        elif ran_num==2:
            b2=Button(r2,text="2",padx=25,pady=15,border=1,background="yellow")
            b2.grid(row=0,column=1,padx=3)
        elif ran_num==3:
            b3=Button(r2,text="3",padx=25,pady=15,border=1,background="yellow")
            b3.grid(row=0,column=2,padx=3)

        elif ran_num==4:
            b4=Button(r2,text="4",padx=25,pady=15,border=1,background="yellow")
            b4.grid(row=0,column=3,padx=3)

        elif ran_num==5:
            b5=Button(r2,text="5",padx=25,pady=15,border=1,background="yellow")
            b5.grid(row=0,column=4,padx=3)
        elif ran_num==6:
            b6=Button(r2,text="6",padx=25,pady=15,border=1,background="yellow")
            b6.grid(row=0,column=5,padx=3)

        elif ran_num==7:
            b7=Button(r2,text="7",padx=25,pady=15,border=1,background="yellow")
            b7.grid(row=0,column=6,padx=3)
        elif ran_num==8:
            b8=Button(r2,text="8",padx=25,pady=15,border=1,background="yellow")
            b8.grid(row=0,column=7,padx=3)

        elif ran_num==9:
            b9=Button(r2,text="9",padx=25,pady=15,border=1,background="yellow")
            b9.grid(row=0,column=8,padx=3)

        elif ran_num==10:
            b10=Button(r2,text="10",padx=25,pady=15,border=1,background="yellow")
            b10.grid(row=0,column=9,padx=3)
        else:
            l2=Label(r2,text="retry")
            l2.grid(row=2,column=0,columnspan=9)
#action3 yellow-------------------END
#action4 for red------------
def active4():
    r=rm.randint(0,11)
    for i in range(1,r,1):
        ran_num=rm.randint(1,11)
        if ran_num==1:
            b1=Button(r2,text="1",padx=25,pady=15,border=1,background="red")
            b1.grid(row=0,column=0,padx=3)
        elif ran_num==2:
            b2=Button(r2,text="2",padx=25,pady=15,border=1,background="red")
            b2.grid(row=0,column=1,padx=3)
        elif ran_num==3:
            b3=Button(r2,text="3",padx=25,pady=15,border=1,background="red")
            b3.grid(row=0,column=2,padx=3)

        elif ran_num==4:
            b4=Button(r2,text="4",padx=25,pady=15,border=1,background="red")
            b4.grid(row=0,column=3,padx=3)

        elif ran_num==5:
            b5=Button(r2,text="5",padx=25,pady=15,border=1,background="red")
            b5.grid(row=0,column=4,padx=3)
        elif ran_num==6:
            b6=Button(r2,text="6",padx=25,pady=15,border=1,background="red")
            b6.grid(row=0,column=5,padx=3)

        elif ran_num==7:
            b7=Button(r2,text="7",padx=25,pady=15,border=1,background="red")
            b7.grid(row=0,column=6,padx=3)
        elif ran_num==8:
            b8=Button(r2,text="8",padx=25,pady=15,border=1,background="red")
            b8.grid(row=0,column=7,padx=3)

        elif ran_num==9:
            b9=Button(r2,text="9",padx=25,pady=15,border=1,background="red")
            b9.grid(row=0,column=8,padx=3)

        elif ran_num==10:
            b10=Button(r2,text="10",padx=25,pady=15,border=1,background="red")
            b10.grid(row=0,column=9,padx=3)
        else:
            l2=Label(r2,text="retry")
            l2.grid(row=2,column=0,columnspan=9)
#action3 red-------------------END
#labels
#button
b1=Button(r2,text="1",padx=25,pady=15,border=1)
b2=Button(r2,text="2",padx=25,pady=15,border=1)
b3=Button(r2,text="3",padx=25,pady=15,border=1)
b4=Button(r2,text="4",padx=25,pady=15,border=1)
b5=Button(r2,text="5",padx=25,pady=15,border=1)

b6=Button(r2,text="6",padx=25,pady=15,border=1)
b7=Button(r2,text="7",padx=25,pady=15,border=1)
b8=Button(r2,text="8",padx=25,pady=15,border=1)
b9=Button(r2,text="9",padx=24,pady=15,border=1)
b10=Button(r2,text="10",padx=24,pady=15,border=1)

b11=Button(r2,text="11",padx=25,pady=15,border=1)
b12=Button(r2,text="12",padx=25,pady=15,border=1)
b13=Button(r2,text="13",padx=25,pady=15,border=1)
b14=Button(r2,text="14",padx=25,pady=15,border=1)
b15=Button(r2,text="15",padx=25,pady=15,border=1)

b16=Button(r2,text="16",padx=25,pady=15,border=1)
b17=Button(r2,text="17",padx=25,pady=15,border=1)
b18=Button(r2,text="18",padx=25,pady=15,border=1)
b19=Button(r2,text="19",padx=24,pady=15,border=1)
b20=Button(r2,text="20",padx=24,pady=15,border=1)

roll1=Button(r2,text="PERSON_1",borderwidth=5,bg="blue",padx=24,pady=15,command=active1)
roll2=Button(r2,text="PERSON_2",borderwidth=5,bg="green",padx=24,pady=15,command=active2)
roll3=Button(r2,text="PERSON_3",borderwidth=5,bg="yellow",padx=24,pady=15,command=active3)
roll4=Button(r2,text="PERSON_4",borderwidth=5,bg="red",padx=24,pady=15,command=active4)
#positions
b1.grid(row=0,column=0,padx=3)
b2.grid(row=0,column=1,padx=3)
b3.grid(row=0,column=2,padx=3)
b4.grid(row=0,column=3,padx=3)
b5.grid(row=0,column=4,padx=3)

b6.grid(row=0,column=5,padx=3)
b7.grid(row=0,column=6,padx=3)
b8.grid(row=0,column=7,padx=3)
b9.grid(row=0,column=8,padx=3)
b10.grid(row=0,column=9,padx=3)




roll1.grid(row=1,column=0,columnspan=2)
roll2.grid(row=1,column=2,columnspan=2)
roll3.grid(row=1,column=4,columnspan=2)
roll4.grid(row=1,column=6,columnspan=2)
#end
r2.mainloop()