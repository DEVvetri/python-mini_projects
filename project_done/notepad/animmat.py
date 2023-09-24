from customtkinter import *

win=CTk()
win.geometry("1920x1080")
win.resizable(1,0)
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
        

animated_view_bar=slidepanel_view(win,0.039,-1)

animated_edit_bar=slidepanel_edit(win,0.039,-1)

animated_file_bar=slidepanel_file(win,0.039,-1)

x=0.5




# #textbox area
# text_box=CTkTextbox(master=win,width=1920,height=900)
# text_box.place(relx=0,rely=0.028)

but_file=CTkButton(master=win,text="file",width=60,fg_color="transparent",hover_color="#696969",command=animated_file_bar.animate)
but_file.place(relx=0.01,rely=0.001)

but_edit=CTkButton(master=win,text="edit",width=60,fg_color="transparent",hover_color="#696969",command=animated_edit_bar.animate)
but_edit.place(relx=0.05,rely=0.001)

but_view=CTkButton(master=win,text="view",width=60,fg_color="transparent",hover_color="#696969",command=animated_view_bar.animate)
but_view.place(relx=0.09,rely=0.001)


#file bar inner buttons
but_newfile=CTkButton(master=animated_file_bar,text="New file     Ctrl+N ",width=60,fg_color="transparent",hover_color="#696969")
but_newfile.place(relx=0.5,rely=0.1,anchor=CENTER)

but_newwin=CTkButton(master=animated_file_bar,text="New Window     Ctrl+shift+N",width=60,fg_color="transparent",hover_color="#696969")
but_newwin.place(relx=0.5,rely=0.18,anchor=CENTER)


but_opem=CTkButton(master=animated_file_bar,text="Open        Ctrl+O",width=60,fg_color="transparent",hover_color="#696969")
but_opem.place(relx=0.5,rely=0.26,anchor=CENTER)

but_save=CTkButton(master=animated_file_bar,text="Save      Ctrl+S",width=60,fg_color="transparent",hover_color="#696969")
but_save.place(relx=0.5,rely=0.34,anchor=CENTER)

but_saveas=CTkButton(master=animated_file_bar,text="Save as       Ctrl+Shift+s",width=60,fg_color="transparent",hover_color="#696969")
but_saveas.place(relx=0.5,rely=0.42,anchor=CENTER)

but_saveall=CTkButton(master=animated_file_bar,text="Save all       Ctrl+Alt+s",width=60,fg_color="transparent",hover_color="#696969")
but_saveall.place(relx=0.5,rely=0.5,anchor=CENTER)

but_page_setup=CTkButton(master=animated_file_bar,text="Page Setup       ",width=60,fg_color="transparent",hover_color="#696969")
but_page_setup.place(relx=0.5,rely=0.58,anchor=CENTER)

but_print=CTkButton(master=animated_file_bar,text="Print       Ctrl+P",width=60,fg_color="transparent",hover_color="#696969")
but_print.place(relx=0.5,rely=0.66,anchor=CENTER)

but_close_tab=CTkButton(master=animated_file_bar,text="Close Tab       CtrlW",width=60,fg_color="transparent",hover_color="#696969")
but_close_tab.place(relx=0.5,rely=0.74,anchor=CENTER)

but_close_win=CTkButton(master=animated_file_bar,text="Close Window       Ctrl+Alt+W",width=60,fg_color="transparent",hover_color="#696969")
but_close_win.place(relx=0.5,rely=0.82,anchor=CENTER)

but_exit=CTkButton(master=animated_file_bar,text="Exit       ",width=60,fg_color="transparent",hover_color="#696969")
but_exit.place(relx=0.5,rely=0.9,anchor=CENTER)



win.mainloop()