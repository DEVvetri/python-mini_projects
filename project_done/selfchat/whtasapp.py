from tkinter import *
#from tkinter.ttk import *
r=Tk()
r.configure(bg="#00ff00")

#functions
def fn_Chat1():
    #r.configure(bg="#00ff66")
#chat1-----------------------------------------------------------------------

    #global variable
    global chat_name1
    chat_name1="Mr_1"
    global l2
    global et_mes_sd_chat1
    global mess1
    #functions
    def to_send_mes1():
        global mess1
        mess1=et_mes_sd_chat1.get()
        et_mes_sd_chat1.delete(0,END)
        send_reader_chat2.delete(0,END)
        send_reader_chat1.delete(0,END)
        send_reader_chat2.insert(0,str(mess1))
        

    def empty_mes_box1():
        send_reader_chat1.delete(0,END)
    #label
    l2=Label(r,text="you are in chat1",font=('arial',10),bg="#00ff00")
    l2m1=Label(r,text="VIEW MESSAGE",font=('arial',10),bg="#00ff00")

    #entry
    et_mes_sd_chat1=Entry(r,width=60,foreground="#ff0000")
    send_reader_chat1=Entry(r,width=60,fg="#ff0000")
    
    #button
    chat_name1=Button(r,text=chat_name1,font=('Arial',15),bd=0,padx=65,bg="#008000")
    send_bt1=Button(r,text="SEND",bd=5,width=20,command=to_send_mes1,bg="#008000")
    Mark_As_Read1=Button(r,text="MARK AS READ",bd=5,width=15,command=empty_mes_box1,bg="#008000")
    #position
    l2.grid(row=2,column=1,columnspan=3)
    chat_name1.grid(row=3,column=0,rowspan=3)
    et_mes_sd_chat1.grid(row=3,column=1,columnspan=2)
    send_bt1.grid(row=4,column=1,columnspan=2,pady=5)
    l2m1.grid(row=5,column=1,columnspan=2)
    send_reader_chat1.grid(row=6,column=1,columnspan=2,pady=5)
    Mark_As_Read1.grid(row=7,column=1,columnspan=2)
    
#chat2-------------------------------------------------------------------
    #r.configure(bg="#00ff66")

    #global variable
    global chat_name2
    chat_name2="Mr_2"
    global l3
    global et_mes_sd_chat2
    global mess2
    #functions
    def to_send_mes2():
        global mess2
        mess2=et_mes_sd_chat2.get()
        et_mes_sd_chat2.delete(0,END)
        send_reader_chat1.delete(0,END)
        send_reader_chat2.delete(0,END)
        send_reader_chat1.insert(0,str(mess2))
    def empty_mes_box2():
        send_reader_chat2.delete(0,END)
     #label
    l3=Label(r,text="you are in chat1",font=('arial',10),bg="#00ff00")
    l3m1=Label(r,text="VIEW MESSAGE",font=('arial',10),bg="#00ff00")

    #entry
    et_mes_sd_chat2=Entry(r,width=60,foreground="#ff0000")
    send_reader_chat2=Entry(r,width=60,foreground="#ff0000")
    
    #button
    chat_name2=Button(r,text=chat_name2,font=('Arial',15),bd=0,padx=65,bg="#008000")
    send_bt2=Button(r,text="SEND",bd=5,width=20,command=to_send_mes2,bg="#008000")
    Mark_As_Read2=Button(r,text="MARK AS READ",bd=5,width=15,command=empty_mes_box2,bg="#008000")
    #position
    l3.grid(row=8,column=1,columnspan=3,pady=5)
    chat_name2.grid(row=9,column=0,rowspan=3)
    et_mes_sd_chat2.grid(row=9,column=1,columnspan=2)
    send_bt2.grid(row=10,column=1,columnspan=2,pady=5)
    l3m1.grid(row=11,column=1,columnspan=2)
    send_reader_chat2.grid(row=12,column=1,columnspan=2,pady=5)
    Mark_As_Read2.grid(row=13,column=1,columnspan=2,pady=5)


def fn_chat2():
    #r.configure(bg="#00ff66")
    #global variable
    global chat_num
    chat_name="Subi"
    global l2
    global et_mes_sd_chat2
    #functions
    #label
    l2=Label(r,text="you are in chat2",font=('arial',10))
    m1=Label(r,text="VIEW MESSAGE",font=('arial',10))

    #entry
    et_mes_sd_chat2=Entry(r,width=60)
    send_reader_chat2=Entry(r,width=60)
    
    #button
    chat_name1=Button(r,text=chat_name,font=('Arial',15),bd=0,padx=65)
    send_bt=Button(r,text="SEND",bd=5,width=30)
    Mark_As_Read=Button(r,text="MARK AS READ",bd=5,width=30)
    
    #position
    l2.grid(row=2,column=0,columnspan=3)
    chat_name1.grid(row=3,column=0,rowspan=3)
    et_mes_sd_chat1.grid(row=3,column=1,columnspan=2)
    send_bt.grid(row=4,column=1,columnspan=2)
    m1.grid(row=5,column=1,columnspan=2)
    send_reader_chat2.grid(row=6,column=1,columnspan=2)
    Mark_As_Read.grid(row=7,column=1,columnspan=2)

def fn_Call():
    l2=Label(r,text="you are in call ",font=('arial',10))
    l2.grid(row=2,column=0,columnspan=3)
#labels
l1=Label(r,text="WhatsApp",font=('arial',20,),padx=209,pady=25,bg="#00ff00")
#buttons
bt_Chat=Button(r,text="Chat",font=('arial',10,),bg="#008000",padx=72,pady=8,command=fn_Chat1)
bt_Status=Button(r,text="Status",font=('arial',10,),bg="#008000",padx=72,pady=8,command=fn_chat2,state="disabled")
bt_Call=Button(r,text="Call",font=('arial',10,),bg="#008000",padx=72,pady=8,command=fn_Call,state="disabled")
#positions
l1.grid(row=0,column=0,columnspan=3)
bt_Chat.grid(row=1,column=0)
bt_Status.grid(row=1,column=1)
bt_Call.grid(row=1,column=2)

#END
r.mainloop()