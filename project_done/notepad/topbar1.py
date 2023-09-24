from customtkinter import *

win=CTk()
# win.geometry("1500x700")
win.iconbitmap("logo.ico")
win.title("NotePad")
win._set_appearance_mode("system")
win.minsize(300,200)
# win.resizable(300,200)
#frame
frame_file=CTkFrame(master=win,width=200,height=400).pack(side=LEFT,anchor=NW)
#inner file frame
frame_file_3=CTkFrame(master=frame_file,width=200,height=230).pack(side=TOP,anchor=NW)
frame_file_1=CTkFrame(master=frame_file,width=200,height=70,fg_color="white").pack(side=TOP,anchor=NW)
frame_file_2=CTkFrame(master=frame_file,width=200,height=90,fg_color="black").pack(side=TOP,anchor=NW)


but_1 =CTkButton(master=frame_file_3,text="New file",hover_color="#696969").pack()
but_2 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_3 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_4 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_5 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_6 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_7 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_8 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_9 =CTkButton(master=frame_file,text="",hover_color="#696969")
but_10=CTkButton(master=frame_file,text="",hover_color="#696969")
but_11=CTkButton(master=frame_file,text="",hover_color="#696969")


but_1 
but_2 
but_3 
but_4 
but_5 
but_6 
but_7 
but_8 
but_9 
but_10
but_11

win.mainloop()