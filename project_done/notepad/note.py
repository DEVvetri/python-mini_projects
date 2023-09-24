from customtkinter import *

win=CTk()
win.geometry("1500x700")
win.iconbitmap("logo.ico")
win.title("NotePad")
win._set_appearance_mode("system")
# win.resizable(0,0)

but_file=CTkButton(master=win,text="file",width=60,fg_color="transparent")
but_edit=CTkButton(master=win,text="edit",width=60,fg_color="transparent")
but_view=CTkButton(master=win,text="view",width=6,fg_color="transparent")
mess=CTkTextbox(master=win,width=1500,height=730)

but_file.grid(row=0,column=0,padx=(0,20))
but_edit.grid(row=0,column=1,padx=(0,40))
but_view.grid(row=0,column=2,padx=(0,20))
mess.grid(row=1,column=0,columnspan=30)
win.mainloop()