from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox
import sqlite3
start=Tk()
start.geometry('1920x1080')
# start.iconbitmap('img\logo.ico')
start.title("Digiket")
#functions
def quit():
    start.destroy()
def start_game():
    start.destroy()
    root=Tk()
    root.geometry("1920x1080")
    # root.iconbitmap("img\logo.ico")
    root.title("digiket")
    root.config(bg="gray")
    #canvas
    my_can=Canvas(root,width=1920,height=1080,bg="gray")
    my_can.place(x=0,y=0)

    #box
    my_can.create_line(340,350,340,550)
    my_can.create_line(1130,350,1130,550)
    my_can.create_line(340,350,1130,350)
    my_can.create_line(340,550,1130,550)

    #left man
    #leg
    my_can.create_line(200,700,250,650)
    my_can.create_line(300,700,250,650)
    #hand
    my_can.create_line(200,640,250,580)
    my_can.create_line(300,640,250,580)
    #body
    my_can.create_line(250,650,250,570)
    #head
    my_can.create_oval(200,450,300,570)

    #face
    my_can.create_oval(220,500,240,510)
    my_can.create_oval(270,500,290,510)

    #right man
    #leg
    my_can.create_line(1200,700,1250,650)
    my_can.create_line(1300,700,1250,650)
    #hand
    my_can.create_line(1200,640,1250,580)
    my_can.create_line(1300,640,1250,580)
    #body
    my_can.create_line(1250,650,1250,570)
    #head
    my_can.create_oval(1200,450,1300,570)
    #face
    my_can.create_oval(1210,500,1230,510)
    my_can.create_oval(1260,500,1280,510)
    #canvas

    #creating databas
    #connecting database
    data=sqlite3.connect('score_board.db')
    #creating cursor
    c=data.cursor()

    #create table "score_board"
    # c.execute(""" CREATE TABLE score_board (
    #            high_score integer
    #           ) """)


    #creating database
    #functions
    def winner():
        if max_score>pri_score:
            messagebox.showinfo("winner is player2")
        elif max_score<pri_score:
            messagebox.showinfo("winner is player1")
        else:
            pass
    def bat_fun():
        global run
        run=random.randint(1,10)
        current=score_ball.get()
        score_bat.delete(0,END)
        score_bat.insert(0,str(run))
        num1=score_bat.get()
        if num1==num_ball:
            # #connecting database
            # data=sqlite3.connect('score_board.db')
        
            # #creating cursor
            # c=data.cursor()
            # #insert values to database
            # c.execute("INSERT INTO score_board VALUES(:high_score)",
            #           {
            #               'high_score':total.get()
            #           } )
            # #selecct  values to database
            # c.execute("SELECT * ,oid FROM score_board ")
            # max_score=str(c.fetchone())
            
            # #save changes
            # data.commit()

            # #close database
            # data.close()
            score_bat.delete(0,END)
            score_bat.insert(0,"WICKET..<'-'>")

            global max_score,pri_score
            max_score=str(total.get()) 
            max_score_label=Label(root,text=max_score+"  ",font=('arial',25),bg="gray").place(x=450,y=450)
            pri_score=max_score

            tot=str(total.get())
            total.delete(0,END)
            total.config(width=11)
            total.insert(0,"GAME OVER")
            score_ball.delete(0,END)
            score_ball.insert(0,"haha losser")
            ball.config(state="disabled")
            bat.config(state="disabled")
            messagebox.showwarning("GAME OVER","batsman loss TOTAL RUN="+tot)
            ball.config(state="disabled")
            pri_score_label=Label(root,text=pri_score+"  ",font=('arial',25),bg="gray").place(x=1000,y=450)
            
        else:
            past=total.get()
            total.delete(0,END)
            total.insert(0,str(int(num1)+int(past)))
        bat.config(state="disabled")
        ball.config(state="active")
    def ball_fun():
        global b
        global num_ball,pri_score
        b=random.randint(1,7)
        current=score_ball.get()
        score_ball.delete(0,END)
        score_ball.insert(0,str(b))
        num_ball=score_ball.get()
        ball.config(state="disabled")
        bat.config(state="active")
        

    def reset():
        score_ball.delete(0,END)
        score_bat.delete(0,END)
        total.delete(0,END)
        total.insert(0,"0")
        bat.config(state="disabled")
        ball.config(state="active")
        b=0
        run=0
    #functions

    #img

    #img
    score_bat=Entry(root,width=20,font=('arial',30))
    score_ball=Entry(root,width=20,font=('arial',30))
    lab_total=Label(root,text="TOTAL",font=('arial',20),bg="gray")
    total=Entry(root,width=10,font=('arial',15))

    player_bating=Label(root,text="BATSMAN",font=('arial',20),bg="gray")
    player_bowling=Label(root,text="BOWLER",font=('arial',20),bg="gray")
    max_name_label=Label(root,text="HIGH SCORE",font=('arial',20),bg="gray")
    target_run_label=Label(root,text="YOUR TAGET",font=('arial',20),bg="gray")

    my_can.create_line(610,600,850,600)
    my_can.create_line(610,650,850,650)

    bat=Button(root,text="HIT",padx=200,pady=10,state="disabled",command=bat_fun)
    ball=Button(root,text="BOWL",padx=200,pady=10,command=ball_fun)
    restart=Button(root,text="RESTART",padx=200,pady=10,command=reset)

    score_bat.place(x=300,y=100)
    score_ball.place(x=750,y=100)

    lab_total.place(x=700,y=157)
    total.place(x=685,y=189)
    total.insert(0,"0")

    player_bating.place(x=450,y=50)
    player_bowling.place(x=900,y=50)
    max_name_label.place(x=400,y=360)
    target_run_label.place(x=900,y=360)

    bat.place(x=300,y=250)
    ball.place(x=750,y=250)
    restart.place(x=500,y=300)

    # #save changes
    # data.commit()

    # #close database
    # data.close()

    root.mainloop()

#buttons
quit_button=Button(start,text="QUIT",bg="red",padx=30,pady=20,bd=10,command=quit).place(x=400,y=300)
start_button=Button(start,text="START",bg="yellow",padx=30,pady=20,bd=10,command=start_game).place(x=1010,y=300)
#labels
start_label1=Label(start,text="HEY GAMER WELCOME",font=('arial',50)).place(x=380,y=200)
start_labe2=Label(start,text="TO DIGIKET",font=('arial',50)).place(x=580,y=300)
start_labe3=Label(start,text="LET\'S PLAY CRICKET ON NUMBERS",font=('arial',50)).place(x=200,y=400)

start.mainloop()