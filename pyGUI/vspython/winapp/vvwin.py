from tkinter import *
#from tkinter.ttk import *
import random
#r2 details
r2=Tk()
r2.geometry('1920x1080')
r2.title("LETS\'S PALY SOME COLORFULL GAMEZZ")
r2.configure(bg="#000000")
#p=PhotoImage(file='')
#r2--functions
def roll_butn_green():
    global r
    r=random.randint(0,20)
    label_roll=Label(r2,text=r)
    label_roll.grid(row=0,column=11)
    if r==1:
        b1=Button(r2,text="1",padx=25,pady=15,bg="#00ff00")
        b1.grid(row=0,column=0)
    elif r==2:
        b2=Button(r2,text="2",padx=25,pady=15,bg="#00ff00")
        b2.grid(row=0,column=1)
    elif r==3:
        b3=Button(r2,text="3",padx=25,pady=15,bg="#00ff00")
        b3.grid(row=0,column=2)
    elif r==4:
        b4=Button(r2,text="4",padx=25,pady=15,bg="#00ff00")
        b4.grid(row=0,column=3)

    elif r==5:
        b5=Button(r2,text="5",padx=25,pady=15,bg="#00ff00")
        b5.grid(row=0,column=4)

    elif r==6:
        b6=Button(r2,text="6",padx=25,pady=15,bg="#00ff00")
        b6.grid(row=0,column=5)

    elif r==7:
        b7=Button(r2,text="7",padx=25,pady=15,bg="#00ff00")
        b7.grid(row=0,column=6)

    elif r==8:
        b8=Button(r2,text="8",padx=25,pady=15,bg="#00ff00")
        b8.grid(row=0,column=7)

    elif r==9:
        b9=Button(r2,text="9",padx=24,pady=15,bg="#00ff00")
        b9.grid(row=0,column=8)

    elif r==10:
        b10=Button(r2,text="10",padx=24,pady=15,bg="#00ff00")
        b10.grid(row=0,column=9)

    elif r==11:
        b11=Button(r2,text="11",padx=23,pady=15,bg="#00ff00")
        b11.grid(row=0,column=11)

    elif r==12:
        b12=Button(r2,text="12",padx=24,pady=15,bg="#00ff00")
        b12.grid(row=0,column=12)

    elif r==13:
        b13=Button(r2,text="13",padx=25,pady=15,bg="#00ff00")
        b13.grid(row=0,column=13)

    elif r==14:
        b14=Button(r2,text="14",padx=25,pady=15,bg="#00ff00")
        b14.grid(row=0,column=14)

    elif r==15:
        b15=Button(r2,text="15",padx=25,pady=15,bg="#00ff00")
        b15.grid(row=0,column=15)

    elif r==16:
        b16=Button(r2,text="16",padx=25,pady=15,bg="#00ff00")
        b16.grid(row=0,column=16)

    elif r==17:
        b17=Button(r2,text="17",padx=25,pady=15,bg="#00ff00")
        b17.grid(row=0,column=17)

    elif r==18:
        b18=Button(r2,text="18",padx=25,pady=15,bg="#00ff00")
        b18.grid(row=0,column=18)

    elif r==19:
        b19=Button(r2,text="19",padx=25,pady=15,bg="#00ff00")
        b19.grid(row=0,column=19)

    elif r==20:
        b20=Button(r2,text="20",padx=25,pady=15,bg="#00ff00")
        b20.grid(row=0,column=20)
    else:
        pass
def roll_butn_yellow():
    global r
    r=random.randint(0,20)
    label_roll=Label(r2,text=r)
    label_roll.grid(row=0,column=11)
    if r==1:
        b1=Button(r2,text="1",padx=25,pady=15,bg="#ffff00")
        b1.grid(row=0,column=0)
    elif r==2:
        b2=Button(r2,text="2",padx=25,pady=15,bg="#ffff00")
        b2.grid(row=0,column=1)
    elif r==3:
        b3=Button(r2,text="3",padx=25,pady=15,bg="#ffff00")
        b3.grid(row=0,column=2)
    elif r==4:
        b4=Button(r2,text="4",padx=25,pady=15,bg="#ffff00")
        b4.grid(row=0,column=3)

    elif r==5:
        b5=Button(r2,text="5",padx=25,pady=15,bg="#ffff00")
        b5.grid(row=0,column=4)

    elif r==6:
        b6=Button(r2,text="6",padx=25,pady=15,bg="#ffff00")
        b6.grid(row=0,column=5)

    elif r==7:
        b7=Button(r2,text="7",padx=25,pady=15,bg="#ffff00")
        b7.grid(row=0,column=6)

    elif r==8:
        b8=Button(r2,text="8",padx=25,pady=15,bg="#ffff00")
        b8.grid(row=0,column=7)

    elif r==9:
        b9=Button(r2,text="9",padx=24,pady=15,bg="#ffff00")
        b9.grid(row=0,column=8)

    elif r==10:
        b10=Button(r2,text="10",padx=24,pady=15,bg="#ffff00")
        b10.grid(row=0,column=9)

    elif r==11:
        b11=Button(r2,text="11",padx=23,pady=15,bg="#ffff00")
        b11.grid(row=0,column=11)

    elif r==12:
        b12=Button(r2,text="12",padx=24,pady=15,bg="#ffff00")
        b12.grid(row=0,column=12)

    elif r==13:
        b13=Button(r2,text="13",padx=25,pady=15,bg="#ffff00")
        b13.grid(row=0,column=13)

    elif r==14:
        b14=Button(r2,text="14",padx=25,pady=15,bg="#ffff00")
        b14.grid(row=0,column=14)

    elif r==15:
        b15=Button(r2,text="15",padx=25,pady=15,bg="#ffff00")
        b15.grid(row=0,column=15)

    elif r==16:
        b16=Button(r2,text="16",padx=25,pady=15,bg="#ffff00")
        b16.grid(row=0,column=16)

    elif r==17:
        b17=Button(r2,text="17",padx=25,pady=15,bg="#ffff00")
        b17.grid(row=0,column=17)

    elif r==18:
        b18=Button(r2,text="18",padx=25,pady=15,bg="#ffff00")
        b18.grid(row=0,column=18)

    elif r==19:
        b19=Button(r2,text="19",padx=25,pady=15,bg="#ffff00")
        b19.grid(row=0,column=19)

    elif r==20:
        b20=Button(r2,text="20",padx=25,pady=15,bg="#ffff00")
        b20.grid(row=0,column=20)
    else:
        pass
def roll_butn_lit_blue():
    global r
    r=random.randint(0,20)
    label_roll=Label(r2,text=r)
    label_roll.grid(row=0,column=11)
    if r==1:
        b1=Button(r2,text="1",padx=25,pady=15,bg="#00ffff")
        b1.grid(row=0,column=0)
    elif r==2:
        b2=Button(r2,text="2",padx=25,pady=15,bg="#00ffff")
        b2.grid(row=0,column=1)
    elif r==3:
        b3=Button(r2,text="3",padx=25,pady=15,bg="#00ffff")
        b3.grid(row=0,column=2)
    elif r==4:
        b4=Button(r2,text="4",padx=25,pady=15,bg="#00ffff")
        b4.grid(row=0,column=3)

    elif r==5:
        b5=Button(r2,text="5",padx=25,pady=15,bg="#00ffff")
        b5.grid(row=0,column=4)

    elif r==6:
        b6=Button(r2,text="6",padx=25,pady=15,bg="#00ffff")
        b6.grid(row=0,column=5)

    elif r==7:
        b7=Button(r2,text="7",padx=25,pady=15,bg="#00ffff")
        b7.grid(row=0,column=6)

    elif r==8:
        b8=Button(r2,text="8",padx=25,pady=15,bg="#00ffff")
        b8.grid(row=0,column=7)

    elif r==9:
        b9=Button(r2,text="9",padx=24,pady=15,bg="#00ffff")
        b9.grid(row=0,column=8)

    elif r==10:
        b10=Button(r2,text="10",padx=24,pady=15,bg="#00ffff")
        b10.grid(row=0,column=9)

    elif r==11:
        b11=Button(r2,text="11",padx=23,pady=15,bg="#00ffff")
        b11.grid(row=0,column=11)

    elif r==12:
        b12=Button(r2,text="12",padx=24,pady=15,bg="#00ffff")
        b12.grid(row=0,column=12)

    elif r==13:
        b13=Button(r2,text="13",padx=25,pady=15,bg="#00ffff")
        b13.grid(row=0,column=13)

    elif r==14:
        b14=Button(r2,text="14",padx=25,pady=15,bg="#00ffff")
        b14.grid(row=0,column=14)

    elif r==15:
        b15=Button(r2,text="15",padx=25,pady=15,bg="#00ffff")
        b15.grid(row=0,column=15)

    elif r==16:
        b16=Button(r2,text="16",padx=25,pady=15,bg="#00ffff")
        b16.grid(row=0,column=16)

    elif r==17:
        b17=Button(r2,text="17",padx=25,pady=15,bg="#00ffff")
        b17.grid(row=0,column=17)

    elif r==18:
        b18=Button(r2,text="18",padx=25,pady=15,bg="#00ffff")
        b18.grid(row=0,column=18)

    elif r==19:
        b19=Button(r2,text="19",padx=25,pady=15,bg="#00ffff")
        b19.grid(row=0,column=19)

    elif r==20:
        b20=Button(r2,text="20",padx=25,pady=15,bg="#00ffff")
        b20.grid(row=0,column=20)
    else:
        pass
def roll_butn_pink():
    global r
    r=random.randint(0,20)
    label_roll=Label(r2,text=r)
    label_roll.grid(row=0,column=11)
    if r==1:
        b1=Button(r2,text="1",padx=25,pady=15,bg="#ff00ff")
        b1.grid(row=0,column=0)
    elif r==2:
        b2=Button(r2,text="2",padx=25,pady=15,bg="#ff00ff")
        b2.grid(row=0,column=1)
    elif r==3:
        b3=Button(r2,text="3",padx=25,pady=15,bg="#ff00ff")
        b3.grid(row=0,column=2)
    elif r==4:
        b4=Button(r2,text="4",padx=25,pady=15,bg="#ff00ff")
        b4.grid(row=0,column=3)

    elif r==5:
        b5=Button(r2,text="5",padx=25,pady=15,bg="#ff00ff")
        b5.grid(row=0,column=4)

    elif r==6:
        b6=Button(r2,text="6",padx=25,pady=15,bg="#ff00ff")
        b6.grid(row=0,column=5)

    elif r==7:
        b7=Button(r2,text="7",padx=25,pady=15,bg="#ff00ff")
        b7.grid(row=0,column=6)

    elif r==8:
        b8=Button(r2,text="8",padx=25,pady=15,bg="#ff00ff")
        b8.grid(row=0,column=7)

    elif r==9:
        b9=Button(r2,text="9",padx=24,pady=15,bg="#ff00ff")
        b9.grid(row=0,column=8)

    elif r==10:
        b10=Button(r2,text="10",padx=24,pady=15,bg="#ff00ff")
        b10.grid(row=0,column=9)

    elif r==11:
        b11=Button(r2,text="11",padx=23,pady=15,bg="#ff00ff")
        b11.grid(row=0,column=11)

    elif r==12:
        b12=Button(r2,text="12",padx=24,pady=15,bg="#ff00ff")
        b12.grid(row=0,column=12)

    elif r==13:
        b13=Button(r2,text="13",padx=25,pady=15,bg="#ff00ff")
        b13.grid(row=0,column=13)

    elif r==14:
        b14=Button(r2,text="14",padx=25,pady=15,bg="#ff00ff")
        b14.grid(row=0,column=14)

    elif r==15:
        b15=Button(r2,text="15",padx=25,pady=15,bg="#ff00ff")
        b15.grid(row=0,column=15)

    elif r==16:
        b16=Button(r2,text="16",padx=25,pady=15,bg="#ff00ff")
        b16.grid(row=0,column=16)

    elif r==17:
        b17=Button(r2,text="17",padx=25,pady=15,bg="#ff00ff")
        b17.grid(row=0,column=17)

    elif r==18:
        b18=Button(r2,text="18",padx=25,pady=15,bg="#ff00ff")
        b18.grid(row=0,column=18)

    elif r==19:
        b19=Button(r2,text="19",padx=25,pady=15,bg="#ff00ff")
        b19.grid(row=0,column=19)

    elif r==20:
        b20=Button(r2,text="20",padx=25,pady=15,bg="#ff00ff")
        b20.grid(row=0,column=20)
    else:
        pass

#r2--widget-frame

#r2--widget-label

#r2--widget-entry


#r2--widget-button
#roll no
roll_but_G=Button(r2,text="ROLL",padx=50,pady=15,bg="#00ff00",command=roll_butn_green)
roll_but_y=Button(r2,text="ROLL",padx=50,pady=15,bg="#ffff00",command=roll_butn_yellow)
roll_but_Lb=Button(r2,text="ROLL",padx=50,pady=15,bg="#00ffff",command=roll_butn_lit_blue)
roll_but_P=Button(r2,text="ROLL",padx=50,pady=15,bg="#ff00ff",command=roll_butn_pink)
#first row
b1=Button(r2,text="1",padx=25,pady=15,border=0)
b2=Button(r2,text="2",padx=25,pady=15,border=0)
b3=Button(r2,text="3",padx=25,pady=15,border=0)
b4=Button(r2,text="4",padx=25,pady=15,border=0)
b5=Button(r2,text="5",padx=25,pady=15,border=0)

b6=Button(r2,text="6",padx=25,pady=15,border=0)
b7=Button(r2,text="7",padx=25,pady=15,border=0)
b8=Button(r2,text="8",padx=25,pady=15,border=0)
b9=Button(r2,text="9",padx=24,pady=15,border=0)
b10=Button(r2,text="10",padx=24,pady=15,border=0)
#safe button
b_safe1=Button(r2,text="safe",bd=10,padx=15,pady=10,bg="#ffff00")
#safe button
b11=Button(r2,text="11",padx=23,pady=15,border=0)
b12=Button(r2,text="12",padx=24,pady=15,border=0)
b13=Button(r2,text="13",padx=25,pady=15,border=0)
b14=Button(r2,text="14",padx=25,pady=15,border=0)
b15=Button(r2,text="15",padx=25,pady=15,border=0)

b16=Button(r2,text="16",padx=25,pady=15,border=0)
b17=Button(r2,text="17",padx=25,pady=15,border=0)
b18=Button(r2,text="18",padx=25,pady=15,border=0)
b19=Button(r2,text="19",padx=25,pady=15,border=0)
b20=Button(r2,text="20",padx=25,pady=15,border=0)
#left column

#right column
#r2--position
#first row
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
#safe
b_safe1.grid(row=0,column=10,padx=20)
#roll
roll_but_G.grid(row=1,column=4,pady=125,columnspan=2)
roll_but_y.grid(row=1,column=14,pady=125,columnspan=2)
roll_but_Lb.grid(row=2,column=4,pady=100,columnspan=2)
roll_but_P.grid(row=2,column=14,pady=100,columnspan=2)

b11.grid(row=0,column=11,padx=3)
b12.grid(row=0,column=12,padx=3)
b13.grid(row=0,column=13,padx=3)
b14.grid(row=0,column=14,padx=3)
b15.grid(row=0,column=15,padx=3)

b16.grid(row=0,column=16,padx=3)
b17.grid(row=0,column=17,padx=3)
b18.grid(row=0,column=18,padx=3)
b19.grid(row=0,column=19,padx=3)
b20.grid(row=0,column=20,padx=3)


#left column

#right column
#end
r2.mainloop()