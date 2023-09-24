from tkinter import *
from tkinter import messagebox
#root-details
root=Tk()
root.title("X,O play panalam")
#root.geometry("500x500")
#x is true
clicked=True
count=0
#functions
def gameover():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b9.config(state=DISABLED)
    b8.config(state=DISABLED)

def re_set():
    global count,clicked
    clicked=True
    count=0
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global play_o,play_x
    b1=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b1))
    b2=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b2))
    b3=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b3))

    b4=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b4))
    b5=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b5))
    b6=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b6))

    b7=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b7))
    b8=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b8))
    b9=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b9))

    play_x=Button(root,text="X YOUR TURN",font=('arial',20),bg="#FFFF00",bd=5,padx=15,command=re_set)
    play_o=Button(root,text="O YOUR TURN",font=('arial',20),bd=5,padx=10,command=re_set)
    #position
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
        
    play_x.grid(row=3,column=0)
    play_o.grid(row=3,column=2)
def whoiswin():
    global win
    win=False
#X start----------------------------------
    #for x win in row alone condition
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="#808000")
        b2.config(bg="#808000")
        b3.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="#808000")
        b5.config(bg="#808000")
        b6.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()  
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="#808000")
        b8.config(bg="#808000")
        b9.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()
    #for x win in column alone condition
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="#808000")
        b4.config(bg="#808000")
        b7.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="#808000")
        b5.config(bg="#808000")
        b8.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="#808000")
        b6.config(bg="#808000")
        b9.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()
#x win daigonal
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="#808000")
        b5.config(bg="#808000")
        b9.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="#808000")
        b5.config(bg="#808000")
        b7.config(bg="#808000")
        win=True
        messagebox.showinfo("GAMER OVER","X won the game")
        gameover()

#X END----------------------------------
#O start----------------------------------
    #for x win in row alone condition
    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="#800000")
        b2.config(bg="#800000")
        b3.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="#800000")
        b5.config(bg="#800000")
        b6.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()  
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="#800000")
        b8.config(bg="#800000")
        b9.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()
    #for x win in column alone condition
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="#800000")
        b4.config(bg="#800000")
        b7.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="#800000")
        b5.config(bg="#800000")
        b8.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="#800000")
        b6.config(bg="#800000")
        b9.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()
#x win daigonal
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="#800000")
        b5.config(bg="#800000")
        b9.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="#800000")
        b5.config(bg="#800000")
        b7.config(bg="#800000")
        win=True
        messagebox.showinfo("GAMER OVER","O won the game")
        gameover()

#O END----------------------------------


def b_click(b):
    global clicked,count
    global play_o,play_x
    global colr
    if b["text"]==" " and clicked==True:
        b["text"]="X"
        b["bg"]="#FFFF00"
        clicked= False
        count+=1
        play_o.config(bg="#FF0000")
        play_x.config(bg="white")
        whoiswin()
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        b["bg"]="#FF0000"
        clicked= True
        count+=1
        play_x.config(bg="#FFFF00")
        play_o.config(bg="white")
        whoiswin()
    else:
        messagebox.showerror("error","this box was already placed..!")
#button


b1=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b1))
b2=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b2))
b3=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b3))

b4=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b4))
b5=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b5))
b6=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b6))

b7=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b7))
b8=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b8))
b9=Button(root,text=" ",font=('arial',20),height=6,width=15,command=lambda:b_click(b9))

re_set=Button(root,text="RESTART GAME",font=('arial',20),bg="#808080",bd=5,padx=5,command=re_set)
play_x=Button(root,text="X YOUR TURN",font=('arial',20),bg="#FFFF00",bd=5,padx=15,command=re_set)
play_o=Button(root,text="O YOUR TURN",font=('arial',20),bd=5,padx=10,command=re_set)
#position
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
#end
play_x.grid(row=3,column=0)
re_set.grid(row=3,column=1)
play_o.grid(row=3,column=2)
root.mainloop()
