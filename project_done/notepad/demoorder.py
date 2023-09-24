from customtkinter import *

win=CTk()
win.geometry("800x700")
win.iconbitmap("logo.ico")
win.title("NotePad")
win._set_appearance_mode("system")
# win.resizable(0,0)
CTkButton(master=win,text="file",width=50,height=10).grid(row=0,column=0,padx=(0,10))
CTkButton(master=win,text="edit",width=50,height=10).grid(row=0,column=1,padx=(0,10))
CTkButton(master=win,text="view",width=50,height=10).grid(row=0,column=2,padx=(0,10))

CTkTextbox(master=win,width=700,height=400).grid(row=1,column=0,columnspan=65)

win.mainloop()