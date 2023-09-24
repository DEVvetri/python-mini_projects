from customtkinter import *
from tkinter import messagebox
root=CTk()
root.minsize(400,300)
root.title("VVpad")
#classes frames

class frame1(CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,height=40)
        
        self.pack(side=TOP,anchor=NW,fill=X,expand=False)

class frame2(CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent)
        
        self.pack(side=TOP,anchor=W,fill=BOTH,expand=True)

class frame3(CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,height=35,fg_color="black")
        
        self.pack(side=TOP,anchor=NW,fill=X,expand=False)

#for file bar
class slidepanel_file(CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)

        self.start_pos=start_pos
        self.end_pos=end_pos
        self.width= 0.12
        #logic
        self.pos=start_pos
        self.in_start_pos=True

    def animate(self):
        if self.in_start_pos:
            self.animate_forword()
        else:
            self.animate_backwards()
    
    def animate_forword(self):
        if self.pos > self.end_pos:
            self.pos-=0.008
            self.place(relx= 0.01,rely=self.pos,relwidth=self.width,relheight=0.5)
            self.after(1,self.animate_forword)
        else:
            self.in_start_pos=False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos+=0.008
            self.place(relx= 0.01,rely=self.pos,relwidth=self.width,relheight=0.5)
            self.after(1,self.animate_backwards)
        else:
            self.in_start_pos=True

#for edit bar
class slidepanel_edit(CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)

        self.start_pos=start_pos
        self.end_pos=end_pos
        self.width= 0.12
        #logic
        self.pos=start_pos
        self.in_start_pos=True

        
    def animate(self):
        if self.in_start_pos:
            self.animate_forword()
        else:
            self.animate_backwards()
    
    def animate_forword(self):
        if self.pos > self.end_pos:
            self.pos-=0.008
            self.place(relx= 0.01,rely=self.pos,relwidth=self.width,relheight=0.5)
            self.after(1,self.animate_forword)
        else:
            self.in_start_pos=False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos+=0.008
            self.place(relx= 0.01,rely=self.pos,relwidth=self.width,relheight=0.5)
            self.after(1,self.animate_backwards)
        else:
            self.in_start_pos=True
              
#for view bar
class slidepanel_view(CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)

        self.start_pos=start_pos
        self.end_pos=end_pos
        self.width= 0.12
        #logic
        self.pos=start_pos
        self.in_start_pos=True

        
    def animate(self):
        if self.in_start_pos:
            self.animate_forword()
        else:
            self.animate_backwards()
    
    def animate_forword(self):
        if self.pos > self.end_pos:
            self.pos-=0.008
            self.place(relx= 0.01,rely=self.pos,relwidth=self.width,relheight=0.5)
            self.after(1,self.animate_forword)
        else:
            self.in_start_pos=False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos+=0.008
            self.place(relx= 0.01,rely=self.pos,relwidth=self.width,relheight=0.5)
            self.after(1,self.animate_backwards)
        else:
            self.in_start_pos=True
        
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


def save():
    file_name=filename.get()
    content=mess.get(1.0,"end-1c")
    count=0
    # for i in file_name:
    #         while i==".":
    if file_name!="" and content!="":
        file=open(f'{file_name}',"w")

        file.write(content)
        file.close()
        messagebox.showinfo("success","successfully saved")
    else:
        messagebox.showerror("error","conditions not accepted")
            # count+=1

#class objects
frame_but=frame1(root)
frame_textbox=frame2(root)
frame_text_down=frame3(root)

#class object anime
animated_file_bar=slidepanel_file(root,0.039,-1)
animated_edit_bar=slidepanel_edit(root,0.039,-1)
animated_view_bar=slidepanel_view(root,0.039,-1)
animated_set_bar=slidepanel_setting(root,1,0.91)
#wudgets stection


but_file=CTkButton(master=frame_but,text="file",width=60,fg_color="transparent",hover_color="#696969",command=animated_file_bar.animate)
but_edit=CTkButton(master=frame_but,text="edit",width=60,fg_color="transparent",hover_color="#696969",command=animated_edit_bar.animate)
but_view=CTkButton(master=frame_but,text="view",width=60,fg_color="transparent",hover_color="#696969",command=animated_view_bar.animate)
filename=CTkEntry(master=frame_but,font=("arial",15),width=200,corner_radius=10,placeholder_text="filename.txt",border_color="black",fg_color="transparent")

but_set=CTkButton(master=frame_but,text="Setting",width=60,fg_color="transparent",hover_color="#696969",command=animated_set_bar.animate)

mess=CTkTextbox(master=frame_textbox,font=("arial",20),corner_radius=0)





line_text=CTkLabel(master=frame_text_down,text="lines 1"+ " column 1")
line_text2=CTkLabel(master=frame_text_down,text=f'|100%             ')
line_text3=CTkLabel(master=frame_text_down,text=f'|Windows (CRLF)       ')
line_text4=CTkLabel(master=frame_text_down,text=f'|UTF-8            ')
#str(len(mess.get("1.0",'end-1c')))


def file_but():
    #file bar inner buttons
    but_newfile=CTkButton(master=animated_file_bar,text="New file     Ctrl+N ",width=60,fg_color="transparent",hover_color="#696969")
    # but_newfile.place(relx=0.5,rely=0.1,anchor=CENTER)
    but_newfile.pack(expand=True)

    but_newwin=CTkButton(master=animated_file_bar,text="New Window     Ctrl+shift+N",width=60,fg_color="transparent",hover_color="#696969")
    # but_newwin.place(relx=0.5,rely=0.18,anchor=CENTER)
    but_newwin.pack(expand=True)

    but_opem=CTkButton(master=animated_file_bar,text="Open        Ctrl+O",width=60,fg_color="transparent",hover_color="#696969")
    # but_opem.place(relx=0.5,rely=0.26,anchor=CENTER)
    but_opem.pack(expand=True)

    but_save=CTkButton(master=animated_file_bar,text="Save      Ctrl+S",width=60,fg_color="transparent",hover_color="#696969")
    # but_save.place(relx=0.5,rely=0.34,anchor=CENTER)
    but_save.pack(expand=True)

    but_saveas=CTkButton(master=animated_file_bar,text="Save as       Ctrl+Shift+s",width=60,fg_color="transparent",hover_color="#696969",command=save)
    # but_saveas.place(relx=0.5,rely=0.42,anchor=CENTER)
    but_saveas.pack(expand=True)

    but_saveall=CTkButton(master=animated_file_bar,text="Save all       Ctrl+Alt+s",width=60,fg_color="transparent",hover_color="#696969")
    # but_saveall.place(relx=0.5,rely=0.5,anchor=CENTER)
    but_saveall.pack(expand=True)

    but_page_setup=CTkButton(master=animated_file_bar,text="Page Setup       ",width=60,fg_color="transparent",hover_color="#696969")
    # but_page_setup.place(relx=0.5,rely=0.58,anchor=CENTER)
    but_page_setup.pack(expand=True)

    but_print=CTkButton(master=animated_file_bar,text="Print       Ctrl+P",width=60,fg_color="transparent",hover_color="#696969")
    # but_print.place(relx=0.5,rely=0.66,anchor=CENTER)
    but_print.pack(expand=True)

    but_close_tab=CTkButton(master=animated_file_bar,text="Close Tab       CtrlW",width=60,fg_color="transparent",hover_color="#696969")
    # but_close_tab.place(relx=0.5,rely=0.74,anchor=CENTER)
    but_close_tab.pack(expand=True)

    but_close_win=CTkButton(master=animated_file_bar,text="Close Window       Ctrl+Alt+W",width=60,fg_color="transparent",hover_color="#696969")
    # but_close_win.place(relx=0.5,rely=0.82,anchor=CENTER)
    but_close_win.pack(expand=True)

    but_exit=CTkButton(master=animated_file_bar,text="Exit       ",width=60,fg_color="transparent",hover_color="#696969")
    # but_exit.place(relx=0.5,rely=0.9,anchor=CENTER)
    but_exit.pack(expand=True)

def edit_but():
    but_edit_1=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_2=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_3=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_4=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_5=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_6=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_7=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_8=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_edit_9=CTkButton(master=animated_edit_bar,text="demo button",fg_color="transparent",hover_color="#696969")

    but_edit_1.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_2.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_3.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_4.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_5.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_6.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_7.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_8.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_edit_9.pack(side=TOP,anchor=CENTER,fill=X,expand=True)

def view_but():
    but_view_1=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_2=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_3=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_4=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_5=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_6=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_7=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_8=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_9=CTkButton(master=animated_view_bar,text="demo button",fg_color="transparent",hover_color="#696969")
    but_view_1.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_2.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_3.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_4.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_5.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_6.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_7.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_8.pack(side=TOP,anchor=CENTER,fill=X,expand=True)
    but_view_9.pack(side=TOP,anchor=CENTER,fill=X,expand=True)

def seting_button():
    but_col_1=CTkButton(master=animated_set_bar,text="blue",width=60,fg_color="transparent",hover_color="#696969",command=lambda:setting_color_change("blue"))
    but_col_2=CTkButton(master=animated_set_bar,text="red",width=60,fg_color="transparent",hover_color="#696969",command=lambda:setting_color_change("red"))
    but_col_3=CTkButton(master=animated_set_bar,text="yellow",width=60,fg_color="transparent",hover_color="#696969",command=lambda:setting_color_change("yellow"))
    but_col_4=CTkButton(master=animated_set_bar,text="white",width=60,fg_color="transparent",hover_color="#696969",command=lambda:setting_color_change("white"))
    but_col_5=CTkButton(master=animated_set_bar,text="green",width=60,fg_color="transparent",hover_color="#696969",command=lambda:setting_color_change("green"))

    but_col_1.pack(side=TOP,expand=True,fill=X)
    but_col_2.pack(side=TOP,expand=True,fill=X)
    but_col_3.pack(side=TOP,expand=True,fill=X)
    but_col_4.pack(side=TOP,expand=True,fill=X)
    but_col_5.pack(side=TOP,expand=True,fill=X)
            
def setting_color_change(b):
    if b=="blue":
        mess.configure(text_color="blue")
    elif b=="red":
        mess.configure(text_color="red")
    elif b=="green":
        mess.configure(text_color="green")
    elif b=="yellow":
        mess.configure(text_color="yellow")
    elif b=="white":
        mess.configure(text_color="white")
    else:
        pass


#button functions calls()

file_but()
edit_but()
view_but()
seting_button()

#position
but_file.pack(side=LEFT)
but_edit.pack(side=LEFT)
but_view.pack(side=LEFT)
filename.pack(side=LEFT,expand=True)
but_set.pack(side=RIGHT,anchor=N)

mess.pack(fill=BOTH,expand=True)

line_text.pack(side=LEFT)
line_text4.pack(side=RIGHT,expand=False)
line_text3.pack(side=RIGHT,expand=False)
line_text2.pack(side=RIGHT,expand=False)

root.mainloop()