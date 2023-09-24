from customtkinter import *

win=CTk()
# win.geometry("1500x700")
win.iconbitmap("logo.ico")
win.title("NotePad")
win._set_appearance_mode("system")
win.minsize(300,200)
# win.resizable(300,200)

#class frame
class slidepanel(CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)

        self.start_pos=start_pos
        self.end_pos=end_pos
        self.width= abs(start_pos-end_pos)

        self.pos=start_pos
        self.in_start_pos=True

        self.place(relx= self.start_pos,rely=self.end_pos,relwidth=self.width,relheight=1)
    def animate(self):
        if self.in_start_pos:
            self.animate_forword()
        else:
            self.animate_backwards()
    
    def animate_forword(self):
        if self.pos > self.end_pos:
            self.pos-=0.008
            self.place(relx= self.pos,rely=0,relwidth=self.width,relheight=1)
            self.after(10),self.animate_forword


    def animate_backwards(self):
        pass

animated_file_bar=slidepanel(win,0.7,1)

but_file=CTkButton(master=win,text="file",width=60,fg_color="transparent",hover_color="#696969",command=animated_file_bar.animate)
but_edit=CTkButton(master=win,text="edit",width=60,fg_color="transparent",hover_color="#696969")
but_view=CTkButton(master=win,text="view",width=60,fg_color="transparent",hover_color="#696969")
mess=CTkTextbox(master=win)

row_col=CTkLabel(master=win,text="lines \n column",font=("arial",10))
row_persent=CTkLabel(master=win,text="| 100% |window(CRLF) |UTF-8",font=("arial",10))

but_file.pack(side=LEFT,anchor=N,fill=X)
but_edit.pack(side=LEFT,anchor=N,fill=X) 
but_view.pack(side=LEFT,anchor=N,expand=False,fill=X)
# row_col.pack(side=BOTTOM,anchor=NW,expand=True)
# row_persent.pack(side=BOTTOM,anchor=NE,expand=True)
mess.pack(side=LEFT,expand=TRUE,anchor=S,fill=BOTH)



# mess.pack(anchor=CENTER,side=LEFT,ipady=290,ipadx=630,expand=True)
win.mainloop()