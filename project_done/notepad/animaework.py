from customtkinter import *

win=CTk()
win.geometry("1920x1080")
win.resizable(1,0)
#for setting bar
class slidepanel_setting(CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)

        self.start_pos=start_pos
        self.end_pos=end_pos
        self.width= 0.09
        #logic
        self.pos=start_pos
        self.in_start_pos=True
        self.h=0.2
    def animate(self):
        if self.in_start_pos:
            self.animate_forword()
        else:
            self.animate_backwards()
    
    def animate_forword(self):
        if self.pos > self.end_pos:
            self.pos-=0.008
            self.place(relx= self.pos,rely=0.04,relwidth=self.width,relheight=self.h)
            self.after(1,self.animate_forword)
        else:
            self.in_start_pos=False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos+=0.008
            self.place(relx= self.pos,rely=0.04,relwidth=self.width,relheight=self.h)
            self.after(1,self.animate_backwards)
        else:
            self.in_start_pos=True
        
animated_set_bar=slidepanel_setting(win,1,0.91)


# #textbox area
# text_box=CTkTextbox(master=win,width=1920,height=900)
# text_box.place(relx=0,rely=0.028)

but_set=CTkButton(master=win,text="Setting",width=60,fg_color="transparent",hover_color="#696969",command=animated_set_bar.animate)
but_set.pack(side=RIGHT,anchor=N)

def seting_button():
    but_col_1=CTkButton(master=animated_set_bar,text="white",width=60,fg_color="transparent",hover_color="#696969")
    but_col_2=CTkButton(master=animated_set_bar,text="red",width=60,fg_color="transparent",hover_color="#696969")
    but_col_3=CTkButton(master=animated_set_bar,text="yellow",width=60,fg_color="transparent",hover_color="#696969")
    but_col_4=CTkButton(master=animated_set_bar,text="gray",width=60,fg_color="transparent",hover_color="#696969")
    but_col_5=CTkButton(master=animated_set_bar,text="green",width=60,fg_color="transparent",hover_color="#696969")

    but_col_1.pack(side=TOP,expand=True,fill=X)
    but_col_2.pack(side=TOP,expand=True,fill=X)
    but_col_3.pack(side=TOP,expand=True,fill=X)
    but_col_4.pack(side=TOP,expand=True,fill=X)
    but_col_5.pack(side=TOP,expand=True,fill=X)
            
seting_button()

win.mainloop()